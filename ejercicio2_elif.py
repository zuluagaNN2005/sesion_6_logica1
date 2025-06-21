# num_1 = float (input("primer numero a consultar"))
# num_2 = float (input("sengundo numero a comentar"))
# operador = input("Que operacion quieres hacer?(+,-,/*): ")

# match operador:
#     case "+":
#         print("resultado",num_1 + num_2)
#     case "-":
#         print("resultado",num_1 - num_2)
#     case "*":
#         print("resultado", num_1 * num_2)
#     case "/":
#         if num_2 != 0:
#             print("resultado", num_1 / num_2)
#         else:
#             print("resultado no valido")
#     case _:
#         print("resultado no valido")        
        
num_1 = float (input("primer numero a consultar"))
num_2 = float (input("sengundo numero a comentar"))
operador = input("Que operacion quieres hacer?(+,-,/*): ")

if operador == "+":
    print("resultado",num_1 + num_2)
    operador == "-"
    print("resultado",num_1 - num_2)
elif     "*" :
    print("resultado", num_1 * num_2)
elif operador == "/":
    if num_2 != 0:
        print("resultado", num_1 / num_2)
    else:
         print("Error diviendo por cero")
else:
        print("operacion no valido.")
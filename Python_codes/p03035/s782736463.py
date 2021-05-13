numerosStr = input().split(" ")
numero=[]
for j in numerosStr:
    numero.append(int(j))

if numero[0] >= 13:
    print(numero[1])
elif numero[0] >= 6 and numero[0] <=12:
    print(int(numero[1]/2))
elif numero[0]<=5:
    print(0)
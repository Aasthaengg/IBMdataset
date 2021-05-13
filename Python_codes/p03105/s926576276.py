numerosStr = input().split(" ")
numeros=[]
for i in numerosStr:
    numeros.append(int(i))

if numeros[1]/numeros[0] > numeros[2]:
    print(int(numeros[2]))
else:
    print(int(numeros[1]/numeros[0]))
    

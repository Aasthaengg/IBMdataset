numerosStr = input().split(" ")
numeros=[]
contador=0
i=0
for j in numerosStr:
    numeros.append(int(j))

A = numeros[0]
B = numeros[1]
T = numeros[2]+0.5

print(int(((T)//A)*B))
n=int(input())
numeros=[int (x) for x in input().split()]
cont=0
for x in range(0,n-2):
    if (numeros[x+1]>numeros[x] and numeros[x+1]<numeros[x+2]) or (numeros[x+1]<numeros[x] and numeros[x+1]>numeros[x+2]):
        if x==n-2:
            break
        cont+=1
print(cont)
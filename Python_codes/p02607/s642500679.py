t= int(input())
lista=[int (x) for x in input().split()]
cont=0
for x in range(len(lista)):
    if x % 2==0:
        if lista[x] % 2 != 0:
            cont+=1
print(cont)
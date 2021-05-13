numero = int(input())
soma = 0
minimo = 100000
for aux in range(numero-1,1,-1):
    prim = str(aux)
    seg = str(numero - aux)
    for x in range(len(prim)):
        soma += int(prim[x])
    for x in range(len(seg)):
        soma += int(seg[x])
    if soma < minimo :
        minimo = soma
    soma = 0
if numero == 2:
    print(numero)
else:
    print(minimo)
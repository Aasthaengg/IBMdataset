a = int(input())
lim = a // 2
soma_lista = []
menor = 100000
for i in range(a - 1, lim, -1):
    b = str(a - abs(i)) + str(abs(i))
    soma = 0
    for digit in b:
        soma += int(digit)
    if soma < menor:
        menor = soma
if a == 2:
    print(a)
else:
    print(menor)

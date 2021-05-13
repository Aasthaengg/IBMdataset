N = int(input())

hurui = [True]*(55556)
for i in range(2, int(55555**0.5)+1):
    for j in range(i*2, 55556, i):
        hurui[j] = False
sosu = []
for i in range(2, 55556):
    if i%5 != 1:
        continue
    if hurui[i]:
        sosu.append(i)

print(*sosu[:N])
k = int(input())
n= 50
lastli = list(range(n))

syo = k//n
amari = k%n

for i in range(len(lastli)):
    lastli[i] += syo

for i in range(amari):
    lastli[i] += n
    for j in range(n):
        if j == i:
            continue
        else:
            lastli[j] -= 1

print(n)
print(*lastli)
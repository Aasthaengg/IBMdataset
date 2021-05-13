table = [0] * (10**5 + 100)

for i in range(2,10**5 + 100):
    if i != 1:
        for j in range(i * 2,10**5 + 100,i):
            table[j] = 1

n = int(input())

while True:
    if table[n] == 0:
        break
    else:
        n += 1

print(n)
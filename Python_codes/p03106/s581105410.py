a, b, k = map(int, input().split())

cds = []
for i in range(1, 101):
    if (a % i == 0) and (b % i == 0):
        cds.append(i)
cds.reverse()
print(cds[k - 1])

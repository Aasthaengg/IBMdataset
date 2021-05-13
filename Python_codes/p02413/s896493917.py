r, c = map(int, input().split())
a = [[0 for i in range(c + 1)] for j in range(r + 1)]

for i in range(r):
    sumC = 0
    ar = input().split()
    for j in range(c):
        a[i][j] = int(ar[j])
        sumC += int(ar[j])
    a[i][c] = sumC

for k in range(c + 1):
    for m in range(r):
        a[r][k] += a[m][k]


for i in a:
    print(*i)

n, m, l = list(map(int, input().split()))

a = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

b = [[0 for j in range(l)] for i in range(m)]
for i in range(m):
    b[i] = list(map(int, input().split()))

c = [[0 for j in range(l)] for i in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]

for i in range(len(c)):
    print(*c[i])


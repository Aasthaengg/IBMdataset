n, m, l = list(map(int, input().split()))

a = [0]*n
b = [0]*m
c = [[0 for col in range(l)] for row in range(n)]

for i in range(n):
    a[i] = list(map(int,input().split()))

for i in range(m):
    b[i] = list(map(int,input().split()))


for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k]*b[k][j]
    print(*c[i])
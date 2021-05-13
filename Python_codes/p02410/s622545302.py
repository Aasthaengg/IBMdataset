[n,m] = map(int, input().split())
a = [[0 for j in range(m)] for i in range(n)]
b = [0 for i in range(m)]

for i in range(n):
    v = list(map(int,input().split()))
    for j in range(m):
        a[i][j] = v[j]

for j in range(m):
    b[j] = int(input())

c = [0 for i in range(n)]

for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]

for i in range(n):
    print(c[i])
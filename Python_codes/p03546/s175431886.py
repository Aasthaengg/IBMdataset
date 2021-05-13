INF = 2**100

h, w = map(int, input().split())
n = 10
d = [[INF for i in range(n)] for j in range(n)]
for i in range(n):
    a = [int(i) for i in input().split()]
    for j in range(n):
        d[i][j] = a[j]
for i in range(n):
    d[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

num = [0] * n
for i in range(h):
    b = [int(j) for j in input().split()]
    for j in b:
        if j != -1:
            num[j] += 1

print(sum([d[i][1]*num[i] for i in range(n)]))
n, m, l = [int(i) for i in input().split()]
d = [[10 ** 18] * n for _ in range(n)]
for i in range(n):
    d[i][i] = 0

for _ in range(m):
    a, b, c = [int(i) for i in input().split()]
    a -= 1
    b -= 1
    d[a][b] = min(d[a][b], c)
    d[b][a] = min(d[b][a], c)

for i in range(n):
    for j in range(n):
        for k in range(n):
            d[j][k] = min(d[j][k], d[j][i] + d[i][k])

d2 = [[10 ** 18] * n for _ in range(n)]
for i in range(n):
    d2[i][i] = 0

for i in range(n):
    for j in range(n):
        if d[i][j] <= l:
            d2[i][j] = min(d2[i][j], 1)

for i in range(n):
    for j in range(n):
        for k in range(n):
            d2[j][k] = min(d2[j][k], d2[j][i] + d2[i][k])

q = int(input())
for _ in range(q):
    s, t = [int(i) - 1 for i in input().split()]
    if d2[s][t] == 10 ** 18:
        print(-1)
    else:
        print(d2[s][t]-1)

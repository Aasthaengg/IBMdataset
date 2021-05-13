n, m = map(int, input().split())

d = [[1001] * n for i in range(n)]

es = []
for i in range(m):
    es.append(list(map(int, input().split())))

for (i, j, w) in es:
    d[i - 1][j - 1] = w
    d[j - 1][i - 1] = w


for k in range(n):
    for i in range(n):
        for j in range(n):
            l = d[i][k] + d[k][j]
            if d[i][j] > l:
                d[i][j] = l

c = 0
for (i, j, w) in es:
    if d[i - 1][j - 1] < w:
        c += 1

print(c)
n, m, l = map(int, input().split())
def warshall_floyd(d, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

inf = 10 ** 15
d = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = min(d[a-1][b-1], c)
    d[b-1][a-1] = min(d[b-1][a-1], c)

warshall_floyd(d, n)

e = [[inf] * n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if d[i][j] <= l:
            e[i][j] = min(e[i][j], 1)
            e[j][i] = min(e[j][i], 1)

warshall_floyd(e, n)


q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    print(e[s-1][t-1] - 1 if e[s-1][t-1] < inf else -1)
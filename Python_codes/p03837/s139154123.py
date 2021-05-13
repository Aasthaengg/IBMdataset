N, M = map(int, input().split())

d = [[10**10]*N for _ in range(N)]

m = {}

for _ in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
    m[(a-1, b-1)] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k] + d[k][j]

ans = 0

for e in m:
    a, b = e
    if d[a][b] < m[e]:
        ans += 1

print(ans)
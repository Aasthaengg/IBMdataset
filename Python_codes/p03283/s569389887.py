n, m, q = map(int, input().split())
edges = [[0]*n for _ in range(n)]

for _ in range(m):
    L, R = map(lambda x: int(x)-1, input().split())
    edges[L][R] += 1


S = [[0]*(n+1)for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        S[i][j+1] = S[i][j] + edges[i][j]

for _ in range(q):
    p, q = map(int, input().split())
    lines = S[p-1:q]
    ans = 0
    for row in lines:
        ans += row[q]-row[p-1]
    print(ans)
from itertools import permutations
INF = float("inf")

n, m, r = map(int, input().split())
r = list(map(lambda x: int(x)-1, input().split()))
g = [[INF] * n for _ in range(n)]
abc = [tuple(map(int, input().split())) for _ in range(m)]
for a, b, c in abc:
    a -= 1; b -= 1
    g[a][b] = c
    g[b][a] = c

def warshall_floyd(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

d = warshall_floyd(g, n)
ans = INF
for route in permutations(r):
    res = 0
    for i in range(1, len(r)):
        res += d[route[i-1]][route[i]]
    ans = min(ans, res)

print(ans)

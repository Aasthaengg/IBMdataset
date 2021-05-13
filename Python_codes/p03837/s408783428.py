inf = 1000 * 1000 + 10

n, m = map(int, input().split())

g = tuple([inf] * n for _ in range(n))
e = set()
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = c
    g[b][a] = c
    e.add((a, b, c))
    e.add((b, a, c))

for i in range(n):
    g[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

res = 0
for a, b, c in e:
    for s in range(n):
        if g[s][b] == g[s][a] + c:
            res += 1
            break

print(m - res // 2)

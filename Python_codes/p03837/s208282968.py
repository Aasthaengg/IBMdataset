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

for i in range(n):
    g[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

# print(g)

need = set()
for a, b, c in e:
    for s in range(n):
        for t in range(n):
            if g[s][t] == g[s][a] + c + g[b][t]:
                need.add((a, b))
                break
        else:
            continue
        break
# print(need)
print(m - len(need))

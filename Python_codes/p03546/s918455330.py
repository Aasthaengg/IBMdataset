h, w = map(int, input().split())

g = []
for _ in range(10):
    a = list(map(int, input().split()))
    g.append(a)

for k in range(10):
    for i in range(10):
        for j in range(10):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

ans = 0
for i in range(h):
    ans += sum(map(lambda x: g[x][1],
                   filter(lambda x: x != -1, map(int, input().split()))))
print(ans)

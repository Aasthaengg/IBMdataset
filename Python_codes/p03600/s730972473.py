import copy
n = int(input())
inf = 10**18
g = [[]]
for i in range(n):
    g.append([0]+list(map(int, input().split())))

g2 = copy.deepcopy(g)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if g[i][k] == 0 or g[k][j] == 0:
                continue
            if g[i][j] == g[i][k] + g[k][j]:
                g[i][j] = 0

ans = 0
for i in range(1, n+1):
    ans += sum(g[i])

for i in range(1, n+1):
    for j in range(1, n+1):
        if g[i][j] == 0:
            g[i][j] = inf
    g[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            g[i][j] = min(g[i][k] + g[k][j], g[i][j])

if g != g2:
    ans = -1

print(ans//2)

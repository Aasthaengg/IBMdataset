def dfs(a, b, f):
    if vis[f] == 1: return
    vis[f] = 1
    for t in V[f]:
        if f!=a or t!=b: dfs(a, b, t)

n, m = map(int, input().split())
E, V = [], [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    E.append([a, b])
    V[a].append(b); V[b].append(a)
ans = 0
for a, b in E:
    vis = [0]*n
    dfs(a, b, a)
    if vis[b] == 0: ans += 1
print(ans)

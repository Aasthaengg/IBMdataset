n, m = map(int, input().split())
E = [[*map(lambda x: int(x)-1, input().split())] for _ in range(m)]

V = [[] for _ in range(n)]
for a, b in E:
    V[a].append(b)
    V[b].append(a)

def dfs(a, b, f):
    if vis[f] == 1: return
    vis[f] = 1
    for t in V[f]:
        if f==a and t == b: continue
        dfs(a, b, t)

ans = 0
for a, b in E:
    vis = [0]*n
    dfs(a, b, a)
    if vis[b] == 0: ans += 1
print(ans)

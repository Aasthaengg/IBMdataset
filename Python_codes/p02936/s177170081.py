import sys
sys.setrecursionlimit(10**6)

def dfs(G, v, p):
    for nv in G[v]:
        if nv == p:
            continue
        point[nv] += point[v]
        dfs(G, nv, v)

n, q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n-1):
    x, y =  map(int, input().split())
    x, y = x-1, y-1
    G[x].append(y)
    G[y].append(x)

point = [0 for _ in range(n)]
for _ in range(q):
    p, x = map(int, input().split())
    point[p-1] += x

dfs(G, 0, -1)
print(*point)
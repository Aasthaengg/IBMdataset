import sys
sys.setrecursionlimit(10**6)

def dfs(G, v):
    seen[v] = True

    for nv in G[v]:
        if seen[nv]:
            continue
        point[nv] += point[v]
        dfs(G, nv)

n, q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n-1):
    x, y =  map(int, input().split())
    x, y = x-1, y-1
    G[x].append(y)
    G[y].append(x)

seen = [False for _ in range(n)]
root = 0
point = [0 for _ in range(n)]
for _ in range(q):
    p, x = map(int, input().split())
    point[p-1] += x

dfs(G, root)
print(*point)
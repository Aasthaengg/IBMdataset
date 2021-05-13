import sys
sys.setrecursionlimit(10**9)
n = int(input())
to = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    to[a].append((b, c))
    to[b].append((a, c))

q, k = map(int, input().split())
dist_k = [0] + [-1] * n
dist_k[k] = 0

def dfs(v):
    for u, du in to[v]:
        if dist_k[u] != -1:
            continue
        dist_k[u] = dist_k[v] + du
        dfs(u)
dfs(k)
dist_xky = [0] * q
for i in range(q):
    x, y = map(int, input().split())
    dist_xky[i] = dist_k[x] + dist_k[y]
print(*dist_xky, sep='\n')
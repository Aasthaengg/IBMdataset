import sys
sys.setrecursionlimit(10 ** 8)
n, q = map(int, input().split())
g = [[] for _ in range(n)]
value = [0] * n
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
for _ in range(q):
    p, x = map(int, input().split())
    value[p-1] += x

seen = [False] * n
def dfs(v):
    seen[v] = True
    for nv in g[v]:
        if seen[nv]:
            continue
        value[nv] += value[v]
        dfs(nv)
dfs(0)
print(*value)
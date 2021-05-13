import sys
sys.setrecursionlimit(1000000)

MOD = 1000000007

def dfs(par, v):
    val = nColors - 1 if par == 0 else nColors - 2
    for child in edges[v]:
        if child != par:
            ways[child] = max(0, val)
            val -= 1
            dfs(v, child)

nVertices, nColors = map(int, input().split())
edges = [[] for _ in range(nVertices + 1)]
for _ in range(nVertices - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

ways = [0] * (nVertices + 1)
ways[1] = nColors
dfs(0, 1)
ret = 1
for w in ways[1:]:
    ret = (ret * w) % MOD
print(ret)

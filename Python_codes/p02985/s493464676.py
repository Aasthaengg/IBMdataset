import sys

sys.setrecursionlimit(100000)

n, k = map(int, input().split())
edges = [[] for _ in range(n)]
for a, b in [map(int, input().split()) for _ in range(n - 1)]:
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

mod = 1000000007
def dfs(v, p, c):
    ret = max(k - c, 0)
    used = 1 + (1 if p >= 0 else 0)
    for w in edges[v]:
        if w != p:
            ret = (ret * dfs(w, v, used)) % mod
            used += 1
    return ret
print(dfs(0, -1, 0))
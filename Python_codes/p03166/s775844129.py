import sys

stdin = sys.stdin
inf = 1 << 60
mod = 1000000007

ni      = lambda: int(ns())
nin     = lambda y: [ni() for _ in range(y)]
na      = lambda: list(map(int, stdin.readline().split()))
nan     = lambda y: [na() for _ in range(y)]
nf      = lambda: float(ns())
nfn     = lambda y: [nf() for _ in range(y)]
nfa     = lambda: list(map(float, stdin.readline().split()))
nfan    = lambda y: [nfa() for _ in range(y)]
ns      = lambda: stdin.readline().rstrip()
nsn     = lambda y: [ns() for _ in range(y)]
ncl     = lambda y: [list(ns()) for _ in range(y)]
nas     = lambda: stdin.readline().split()

sys.setrecursionlimit(10 ** 6)

n, m = na()
xy = nan(m)

g = [[] for _ in range(n)]
for i in range(m):
    x, y = xy[i]
    x -= 1
    y -= 1
    g[x].append(y)

dp = [-1] * (n + 1)

def dfs(v):
    if dp[v] != -1:
        return dp[v]
    res = 0
    for nv in g[v]:
        res = max(res, dfs(nv) + 1)
    dp[v] = res
    return dp[v]

ans = 0
for v in range(n):
    ans = max(ans, dfs(v))

print(ans)
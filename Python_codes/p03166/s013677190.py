import sys
sys.setrecursionlimit(10000)

def solve(g):
    dp = [-1]*len(g)
    def _solve(f):
        if dp[f] == -1:
            dp[f] = 0
            for c in g[f]:
                dp[f] = max(dp[f], 1 + _solve(c))
        return dp[f]
    for f in range(len(g)):
        _solve(f)
    # print(dp)
    return max(dp)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    f, t = map(int, input().split())
    g[f-1].append(t-1)

print(solve(g))

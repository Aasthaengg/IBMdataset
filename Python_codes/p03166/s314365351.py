import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**7)
def LPP():
    n, m = map(int, readline().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        s, t = map(int, readline().split())
        s -= 1
        t -= 1
        edges[s].append(t)
    dp = [-1]*n
    def dfs(s):
        if dp[s] != -1:
            return dp[s]
        if len(edges[s]) == 0:
            dp[s] = 0
            return 0
        res = 0
        for t in edges[s]:
            res = max(res, dfs(t)+1)
        dp[s] = res
        return res
    for i in range(n):
        dfs(i)
    print(max(dp),end="")

LPP()


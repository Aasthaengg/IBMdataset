import sys
sys.setrecursionlimit(11000)
def util(adj, curr, dp):
    res = 0
    if dp[curr] != -1:
        return dp[curr]
    for next in adj[curr]:
        res = max(res,1 + util(adj, next, dp))
    dp[curr] = res
    return res
 
n, m = map(int, input().strip().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().strip().split())
    adj[x - 1].append(y - 1)
dp = [-1]*n
lp = 0
for i in range(n):
    lp = max(lp, util(adj, i, dp))
print(lp)
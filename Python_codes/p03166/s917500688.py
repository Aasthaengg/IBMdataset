import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
dp = [-1]*(n+1)
path = [[] for i in range(n)]
X = []; Y = []
for i in range(m):
    x, y = map(int, input().split())
    X.append(x-1); Y.append(y-1)
    path[x-1].append(y-1)

def dfs(i):
    if dp[i]>0: return dp[i]
    res = 0
    for k in path[i]:
        res = max(res, dfs(k)+1)
    dp[i] = res
    return res

ans = 0
for i in range(n):
    ans = max(ans, dfs(i))
print(ans)
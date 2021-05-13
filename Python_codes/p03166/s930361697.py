import sys
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())
g = [[] for i in range(n)]
dp = [-1] * n
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    g[x].append(y)



def rec(v):
    if dp[v] != -1:
        return dp[v]
    
    res = 0
    for i in g[v]:
        res = max(res, rec(i) + 1)
    
    dp[v] = res
    return dp[v]

for i in range(n):
    rec(i)
print(max(dp))

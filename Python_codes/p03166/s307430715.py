import sys
sys.setrecursionlimit(10**5+10)
def memo(v):
    if dp[v]!=-1:return dp[v]
    ans = 0
    for next_v in g[v]:
        ans = max(ans,memo(next_v)+1)
    dp[v] = ans
    return ans

n,m = map(int,input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    g[x].append(y)
    
dp = [-1]*(n+1)

ans = 0
for v in range(1,n+1):
    ans = max(ans, memo(v))
    
print(ans)

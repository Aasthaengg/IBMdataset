import sys

sys.setrecursionlimit(10**9)
INF=float('inf')

n,m=map(int,input().split())
adj=[[] for _ in range(n+1)]
for _ in range(m):
  x,y=map(int,input().split())
  adj[x].append(y)
  
dp=[-1 for _ in range(n+1)]

def f(k):
  if dp[k]!=-1:
    return dp[k]
  
  dp[k]=0
  if adj[k]:
    for v in adj[k]:
      dp[k]=max(dp[k],f(v)+1)
  return dp[k]

ans=-INF  
for i in range(1,n+1):
  ans=max(ans,f(i))

print(ans)
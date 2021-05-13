import sys

sys.setrecursionlimit(10**9)
n,m=map(int,input().split())

g=[[] for i in range(n)]
for i in range(m):
  v1,v2=map(int,input().split())
  v1-=1;v2-=1
  g[v1].append(v2)

dp=[-1]*n  
  
def dfs(i):
  if dp[i]!=-1:
    return dp[i]
  temp=0
  for nv in g[i]:
    temp=max(temp,dfs(nv)+1)
  dp[i]=temp  
  return temp  
    
res=0
for i in range(n):
  res=max(res,dfs(i))
print(res)

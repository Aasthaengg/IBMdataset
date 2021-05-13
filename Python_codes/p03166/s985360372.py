import sys
sys.setrecursionlimit(10**8)
n,m=map(int,input().split())
adjacent_list=[[] for i in range(n+1)]
for i in range(m):
  x,y=map(int,input().split())
  adjacent_list[x].append(y)

#print(adjacent_list)

dp=[-1]*(n+1)

def dfs(i):
  if dp[i]!=-1:
    return dp[i]
  res=0
  for j in adjacent_list[i]:
    res=max(res,dfs(j)+1)
  dp[i]=res
  return dp[i]
ans=0
for i in range(1,n+1):
  ans=max(ans,dfs(i))
  
print(ans)
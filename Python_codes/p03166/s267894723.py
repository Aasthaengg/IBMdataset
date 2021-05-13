import sys
sys.setrecursionlimit(10**9)
def dfs(a,adjl,visited,dp):
  for i in adjl[a]:
    if visited[i]==0:
      visited[i]=1
      dfs(i,adjl,visited,dp)
 
    dp[a]=max(dp[a],1+dp[i])
n,m=map(int,input().split())
li=[]
for i in range(m):
  li.append([int(k) for k in input().split()])
adjl=[[] for j in range(n+1)]
for k in range(len(li)):
  adjl[li[k][0]].append(li[k][1])
visited=[0]*(n+1)
dp=[0]*(n+1)
for a in range(1,n+1):
  if visited[a]==0:
    visited[a]=1
    dfs(a,adjl,visited,dp)
print(max(dp))

  
  

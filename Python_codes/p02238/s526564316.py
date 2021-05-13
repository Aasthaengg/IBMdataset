n=int(input())
edge=[[] for _ in range(n+1)]
for i in range(n):
  v,k,*u=list(map(int,input().split()))
  edge[v]=u
d=[0]*(n+1)
f=[0]*(n+1)
def dfs(now,t):
  d[now]=t
  vis.append(now)
  for i in edge[now]:
    if i not in vis:
      t=dfs(i,t+1)
  f[now]=t+1
  return t+1
vis=[]
t=1
for i in range(1,n+1):
  if i not in vis:
    t=dfs(i,t)+1
for i in range(1,n+1):
  print(i,d[i],f[i])

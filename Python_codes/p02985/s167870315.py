n,k=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n-1)]
connection=[[] for i in range(n)]
for i in range(n-1):
  connection[l[i][0]-1].append(l[i][1]-1)
  connection[l[i][1]-1].append(l[i][0]-1)
mod=10**9+7

def bfs(v):
  child=[0]*n
  next=[v]
  next2=set()
  visited=[-1]*n
  visitct=0
  while len(next)!=0 and visitct!=n:
    for i in range(len(next)):
      if visited[next[i]]==-1:
        visited[next[i]]=1
        visitct+=1
        for j in range(len(connection[next[i]])):
          if visited[connection[next[i]][j]]==-1:
            child[next[i]]+=1
            next2.add(connection[next[i]][j])
    next=list(next2)
    next2=set()
  return child

child=bfs(0)
ans=k
for i in range(n):
  if i==0:
    for j in range(k-1,k-1-child[i],-1):
      ans*=j
      ans%=mod
  else:
    for j in range(k-2,k-2-child[i],-1): 
      ans*=j
      ans%=mod
print(ans%mod)
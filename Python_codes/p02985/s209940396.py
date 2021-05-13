n,k=map(int,input().split())
path=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  path[a-1].append(b-1)
  path[b-1].append(a-1)
mod=10**9+7
stack=[0]
visited=[1]+[0]*(n-1)
ans=k
while stack:
  v=stack.pop(0)
  c=k-2 if v!=0 else k-1
  for d in path[v]:
    if visited[d]:
      continue
    visited[d]=1
    ans=(ans*c)%mod
    c-=1
    stack.append(d)
print(ans)
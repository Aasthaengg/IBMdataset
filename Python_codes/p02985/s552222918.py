n,k=map(int,input().split())
mod=10**9+7
tree=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  tree[a-1].append(b-1)
  tree[b-1].append(a-1)
stack=[0]
visited=[True]+[False]*n
ans=k
while stack:
  v=stack.pop()
  c=k-2 if v!=0 else k-1
  for i in tree[v]:
    if not visited[i]:
      ans=(ans*c)%mod
      c-=1
      stack.append(i)
      visited[i]=True
print(ans)
N=int(input())
links=[set() for _ in [0]*N]
for i in range(1,N):
  u,v,w=map(int,input().split())
  u-=1
  v-=1
  links[u].add((v,w))
  links[v].add((u,w))
ans=[-1]*N
q=[(0,0,-1)]
while q:
  v,d,p=q.pop()
  if d%2==0:
    ans[v]=0
  else:
    ans[v]=1
  for u,w in links[v]:
    if u==p:
      continue
    q.append((u,w+d,v))
print('\n'.join(map(str,ans)))
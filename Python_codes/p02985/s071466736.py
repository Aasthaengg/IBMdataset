n,k=map(int,input().split())
e=[[]for _ in range(n+1)]
for _ in range(n-1):
  a,b=map(int,input().split())
  e[a]+=[b]
  e[b]+=[a]
mod=10**9+7
vis=[1]*(n+1)
vis[1]=0
q=[1]
ans=k
while q:
  now=q.pop()
  i=0
  for to in e[now]:
    if vis[to]:
      vis[to]=0
      ans*=max(k-i-1-(now!=1),0)
      ans%=mod
      q+=[to]
      i+=1
print(ans)
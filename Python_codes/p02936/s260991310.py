f=lambda:map(int,input().split())
n,k=f()
g=[[] for _ in range(n)]
for _ in range(n-1):
  a,b=f()
  g[a-1]+=[b-1]
  g[b-1]+=[a-1]
l=[0]*n
for _ in range(k):
  p,x=f()
  l[p-1]+=x
u=[0]*n
q=[0]
while q:
  v=q.pop()
  u[v]=1
  for c in g[v]:
    if u[c]: continue
    l[c]+=l[v]
    q+=[c]
print(*l)
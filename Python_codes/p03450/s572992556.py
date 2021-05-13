n,m=map(int,input().split())
INF=10**18
e=[[]for _ in range(n+1)]
for _ in range(m):
  l,r,d=map(int,input().split())
  e[l]+=[(r,d)]
  e[r]+=[(l,-d)]
d=[INF]*(n+1)
for i in range(n+1):
  if d[i]!=INF:continue
  d[i]=0
  q=[i]
  while q:
    now=q.pop()
    for to,dist in e[now]:
      if d[to]==INF:
        d[to]=d[now]+dist
        q+=[to]
      else:
        if d[to]!=d[now]+dist:
          print('No')
          exit()
print('Yes')
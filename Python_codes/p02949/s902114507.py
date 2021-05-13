n,m,p=map(int,input().split())
E=[list(map(int,input().split())) for i in range(m)]
INF=float("inf")
dist=[INF]*n
dist[0]=0
prev=0
# 閉路の長さの最大はnなので2*n回ループさせれば閉路検出ができる
for i in range(2*n):
  for fr,to,cost in E:
    fr,to=fr-1,to-1
    cost*=-1
    cost+=p
    if dist[fr]!=INF and dist[to]>dist[fr]+cost:
      dist[to]=dist[fr]+cost
      if i>=n:
        dist[to]=-float("inf")
    if i==n-1:
      prev=dist[n-1]
if prev==dist[n-1]:
  print(max(-dist[n-1],0))
else:
  print(-1)

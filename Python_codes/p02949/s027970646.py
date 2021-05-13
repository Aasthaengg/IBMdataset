def shortest_path(s):
  dist[s]=0
  for _ in range(n):
    for fr,to,cost in edge:
      if dist[fr]!=inf and dist[to]>dist[fr]+cost:
        dist[to]=dist[fr]+cost

def find_negative_loops():
  for _ in range(n):
    for fr,to,cost in edge:
      if dist[fr]!=inf and dist[to]>dist[fr]+cost:
        dist[to]=dist[fr]+cost
        negative[to]=True
      if negative[fr]:negative[to]=True

n,m,p=map(int,input().split())
edge=[]
for i in range(m):
  a,b,c=map(int,input().split())
  edge.append([a-1,b-1,-c+p])
inf=float("inf")
dist=[inf]*n
negative=[False]*n
shortest_path(0)
find_negative_loops()
print(-1) if negative[-1] else print(max(-dist[-1],0))

import copy

def Warshall_Floyd(edges,N):
  for k in range(N):
    for i in range(N):
      for j in range(N):
        edges[i][j]=min(edges[i][j],edges[i][k]+edges[k][j])
  return edges

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
g=[[float('inf')]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    g[i][j]=arr[i][j]
d=Warshall_Floyd(copy.deepcopy(g),n)
ans=0
for a in range(n):
  for b in range(n):
    if a>=b:
      continue
    w=g[a][b]
    if d[a][b]<w:
      print(-1)
      exit()
    else:
      tmp=10**10
      for k in range(n):
        if k==a or k==b:
          continue
        tmp=min(tmp,d[a][k]+d[k][b])
      if w==tmp:
        continue
      else:
        ans+=w
else:
  print(ans)

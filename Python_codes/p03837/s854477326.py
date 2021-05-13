import os,io
import heapq
INF=10**9
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline  
n,m=map(int,input().split())
edges=[]
d=[]
for i in range(n+1):
  d.append([])
  for j in range(n+1):
    d[-1].append(INF)
  d[i][i]==0
for i in range(m):
  a,b,c=list(map(int,input().split()))
  edges.append([a,b,c])
  d[a][b]=c
  d[b][a]=c
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if (d[i][j]>d[i][k]+d[k][j]):
        d[i][j]=d[i][k]+d[k][j]
ans=0
for i in range(m):
  a=edges[i][0]
  b=edges[i][1]
  c=edges[i][2]
  if d[a][b]<c:
    ans+=1
print(ans)
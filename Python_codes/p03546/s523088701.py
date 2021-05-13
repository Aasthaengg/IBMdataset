H,W=map(int,input().split())
weight=[list(map(int,input().split())) for _ in range(10)]
graph=[[i for i in range(10)] for j in range(10)]
for i in range(10):
  graph[i].pop(i)
import math
import heapq

d=[math.inf for i in range(10)]
d[1]=0
q=[]
heapq.heappush(q,1)
while q:
  v=heapq.heappop(q)
  for u in graph[v]:
    if weight[u][v]+d[v]<d[u]:
      d[u]=weight[u][v]+d[v]
      heapq.heappush(q,u)
A=[list(map(int,input().split())) for _ in range(H)]

dic={}
for i in range(H):
  for j in range(W):
    if A[i][j]!=-1:
      if A[i][j] in dic:
        dic[A[i][j]]+=1
      else:
        dic[A[i][j]]=1
ans=0
for k,v in dic.items():
  ans+=d[k]*v
print(ans)
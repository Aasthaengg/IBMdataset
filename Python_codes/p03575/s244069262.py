N,M=map(int,input().split())
graph=[]
def find(x):
  if par[x]==x:
    return x
  else:
    par[x]=find(par[x])
    return par[x]
def union(a,b):
  x=find(a)
  y=find(b)
  if x!=y:
    if size[x]<size[y]:
      par[x]=par[y]
      size[y]+=size[x]
    else: 
      par[y]=par[x]
      size[x]+=size[y]
  else:
    return
for i in range(M):
  a,b=map(int,input().split())
  graph.append((a-1,b-1))
bridge=0
from collections import Counter
for i in range(M):
  par=[i for i in range(N)]
  size=[1 for i in range(N)] 
  for j in range(M):
    if j!=i:
      union(graph[j][0],graph[j][1])
  if N not in size:
    bridge+=1
print(bridge)
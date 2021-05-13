from collections import deque

N,M=map(int,input().split())
edge=[[] for _ in range(N+1)]

for i in range(M):
  A,B=map(int,input().split())
  edge[A].append(B)
  edge[B].append(A)

  
dist=[-1]*(N+1)
d=deque([1])

while d:
  x = d.popleft()
  for i in range(len(edge[x])):
    if dist[edge[x][i]]==-1:
      dist[edge[x][i]]=x
      d.append(edge[x][i])

print("Yes")
print(*dist[2:],sep='\n')

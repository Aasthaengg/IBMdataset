def MI():  return map(int, input().split())
N,Q=MI()
graph=[[] for i in range(N)]
for i in range(1,N):
  a,b=MI()
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)
point=[0]*N  
for i in range(Q):
  p,x=MI()
  point[p-1]+=x
import collections
q=collections.deque()
q.append(0)
check=[0]*N
check[0]=1
while len(q)>0:
  v=q.pop()
  check[v]=1
  for u in graph[v]:
    if check[u]==1:
      continue
    point[u]+=point[v]
    q.append(u)
print(*point)
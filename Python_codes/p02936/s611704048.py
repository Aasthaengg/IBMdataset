from collections import deque
def MI(): return map(int, input().split())
N,Q=MI()
graph=[[] for i in range(N)]
Point=[0]*N
for i in range(N-1):
  a,b=MI()
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)
for i in range(Q):
  p,x=MI()
  Point[p-1]+=x
que=deque([])
que.append(0)
check=[0]*N
while que:
  v=que.pop()
  check[v]=1
  for u in graph[v]:
    if check[u]!=1:
      #continue
      Point[u]+=Point[v]
      que.append(u)
print(*Point)
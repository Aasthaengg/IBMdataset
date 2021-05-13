import collections
def MI(): return map(int, input().split())
N,Q=MI()
Edge=[[] for _ in range(N)]
Point=[0]*(N)
for _ in range(N-1):
  a,b=MI()
  Edge[a-1].append(b-1)
  Edge[b-1].append(a-1)
for _ in range(Q):
  p,x=MI()
  Point[p-1]+=x
check=[0]*N
que=collections.deque()
que.append(0)
while que:
  v=que.popleft()
  check[v]=1
  for u in Edge[v]:
    if check[u]==1:
      continue    
    Point[u]+=Point[v]
    que.append(u)  
'''
def dfs(now,pre=-1):
  for nxt in Edge[now]:
    if nxt==pre:
      continue
    Point[nxt]+=Point[now]
    #print(*Point)
    dfs(nxt,now)
dfs(0)
'''
print(*Point)
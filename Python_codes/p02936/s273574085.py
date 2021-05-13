import sys
sys.setrecursionlimit(10**6)

def MI(): return map(int, input().split())

N,Q=MI()
Edge=[[] for _ in range(N)]
Point=[0]*N

for i in range(N-1):
  a,b=MI()
  Edge[a-1].append(b-1)
  Edge[b-1].append(a-1)

for i in range(Q):
  p,x=MI()
  Point[p-1]+=x

def dfs(now,pre=-1):
  for nxt in Edge[now]:
    if nxt==pre:
      continue
    Point[nxt]+=Point[now]
    dfs(nxt,now)
dfs(0)
print(*Point)
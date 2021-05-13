import sys
sys.setrecursionlimit(10**6)
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
def dfs(now,pre=-1):  
  for next in graph[now]:
    if next==pre:
      continue
    point[next]+=point[now]
    dfs(next,now)
dfs(0)
print(*point)
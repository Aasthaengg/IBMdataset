N, M = map(int, input().split())
edge = [[] for _ in range(N)]
to = [False]*N
for i in range(M):
  a,b = map(int, input().split())
  edge[a-1].append(b-1)
  to[b-1] = True

import sys
sys.setrecursionlimit(10**8)

def dfs(v):
  if lis[v]>=0:
    return lis[v]
  if len(edge[v])==0:
    lis[v] = 1
    return 1
  ans = 0
  for u in edge[v]:
    ans = max(ans, dfs(u))
  lis[v] = ans+1
  return ans+1

ans = 0
lis = [-1]*N
for r in range(N):
  if to[r]==False:
    ans = max(ans, dfs(r)-1)
print(ans)
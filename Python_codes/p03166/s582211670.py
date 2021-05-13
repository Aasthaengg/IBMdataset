import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
  a,b = map(int, input().split())
  edge[a-1].append(b-1)

def dfs(v):
  if len(edge[v])==0:
    return 0
  ans = 0
  for u in edge[v]:
    if longest[u]==-1:
      longest[u]=dfs(u)
    ans = max(ans,longest[u]+1)
  return ans

longest = [-1]*N
for i in range(N):
  if longest[i]==-1:
    longest[i] = dfs(i)
ans = max(longest)
print(ans)
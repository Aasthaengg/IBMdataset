N = int(input())
edge = [[] for _ in range(N)]
for i in range(N-1):
  a,b = map(int, input().split())
  edge[a-1].append(b-1)
  edge[b-1].append(a-1)
C = sorted(list(map(int, input().split())))
M = sum(C[:-1])
import sys
sys.setrecursionlimit(10**8)

def dfs(v):
  for u in edge[v]:
    if nums[u]==-1:
      nums[u]=C.pop(-1)
      dfs(u)
  return 0

nums = [-1]*N
nums[0] = C.pop(-1)
dfs(0)

print(M)
print(*nums)
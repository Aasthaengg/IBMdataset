import sys
sys.setrecursionlimit(10 ** 9)
import heapq

N = int(input())
E = [list(map(lambda x: int(x)-1,input().split())) for _ in range(N-1)]
C = sorted(list(map(lambda x: int(x)*(-1),input().split())))
m = -sum(C[1:])
heapq.heapify(C)

V = [set() for _ in range(N)]
for u,v in E:
  V[u].add(v)
  V[v].add(u)

A = [0 for _ in range(N)]
def dfs(v,s):
  A[v] = -heapq.heappop(C)
  for u in V[v]:
    if u != s:
      dfs(u,v)
dfs(0,-1)

print(m)
print(*A)

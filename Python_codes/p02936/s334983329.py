import sys
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
T = [[] for _ in range(N)]

for i in range(N-1):
  a, b = map(int, input().split())
  T[a-1].append(b)
  T[b-1].append(a)
PX = [list(map(int, input().split())) for _ in range(Q)]
C = [0 for _ in range(N)]
for p, x in PX:
  C[p-1] += x

def dfs(node, previousNode, previousPoint):
  C[node-1] += previousPoint
  for next in T[node-1]:
    if next != 1 and next != previousNode:
      dfs(next, node, C[node-1])
dfs(1, 0, 0)
print(" ".join(map(str, C)))
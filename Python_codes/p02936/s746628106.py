import sys
readline = sys.stdin.readline

N,Q = map(int,readline().split())

G = [[] for i in range(N)]
for i in range(N - 1):
  a,b = map(int,readline().split())
  G[a - 1].append(b - 1)
  G[b - 1].append(a - 1)

P = [0] * N
for i in range(Q):
  p,x = map(int,readline().split())
  P[p - 1] += x
  
ans = [0] * N

stack = []
# 頂点, 親, そこまでの点数
stack.append([0, -1, 0])
while stack:
  v,parent,point = stack.pop()
  point += P[v]
  ans[v] = point
  for child in G[v]:
    if child == parent:
      continue
    stack.append([child, v, point])
  
print(*ans)
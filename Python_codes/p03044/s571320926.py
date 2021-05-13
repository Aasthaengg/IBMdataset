import sys
readline = sys.stdin.readline

# スタートを0で塗り、行先が奇数であれば違う色で塗る、を繰り返せばよい
N = int(readline())
G = [[] for i in range(N)]

for i in range(N - 1):
  u,v,w = map(int,readline().split())
  G[u - 1].append([v - 1, w])
  G[v - 1].append([u - 1, w])

ans = [-1] * N

stack = []
# 頂点, 色
stack.append([0,0])
while stack:
  v,color = stack.pop()
  if ans[v] != -1:
    continue
  ans[v] = color
  for child in G[v]:
    col = color
    if child[1] % 2 == 1:
      col ^= 1
    stack.append([child[0], col])

for a in ans:
  print(a)
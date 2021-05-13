# 全ての頂点について、フェネックからの距離とすぬけくんからの距離を求める
# フェネックからの距離 <= すぬけくんから距離　の頂点は黒　そうでなければ白

import sys
readline = sys.stdin.readline

N = int(readline())
G = [[] for i in range(N)]
for i in range(N - 1):
  a,b = map(int,readline().split())
  G[a - 1].append(b - 1)
  G[b - 1].append(a - 1)
  
dist_from_fen = [-1 for i in range(N)]
dist_from_snk = [-1 for i in range(N)]

stack = []
# 頂点、距離、親
stack.append([0,0,-1])
while stack:
  v,dist,parent = stack.pop()
  dist_from_fen[v] = dist
  for child in G[v]:
    if child == parent:
      continue
    stack.append([child,dist + 1,v])

stack = []
stack.append([N - 1,0,-1])
while stack:
  v,dist,parent = stack.pop()
  dist_from_snk[v] = dist
  for child in G[v]:
    if child == parent:
      continue
    stack.append([child,dist + 1,v])

black = 0
white = 0
for i in range(N):
  if dist_from_fen[i] <= dist_from_snk[i]:
    black += 1
  else:
    white += 1
print(("Snuke","Fennec")[black > white])
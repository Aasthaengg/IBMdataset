import sys
readline = sys.stdin.readline

# 全探索
N,M = map(int,readline().split())
G = [[] for i in range(N)]
bridges = [None] * M
for i in range(M):
  a,b = map(int,readline().split())
  G[a - 1].append(b - 1)
  G[b - 1].append(a - 1)
  bridges[i] = (a - 1,b - 1)
  
ans = 0
for i in range(M):
  # 使わない橋を決める
  NG = bridges[i]
  seen = set()
  stack = []
  # 頂点, 親
  stack.append([0, -1])
  while stack:
    v,parent = stack.pop()
    if v in seen:
      continue
    seen.add(v)
    for child in G[v]:
      if child == parent:
        continue
      if (v, child) == NG or (child, v) == NG: # 今回使わない橋
        continue
      stack.append([child, v])
  if len(seen) != N:
    ans += 1

print(ans)
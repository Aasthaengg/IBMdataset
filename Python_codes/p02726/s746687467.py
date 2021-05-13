import sys
readline = sys.stdin.readline

N,X,Y = map(int,readline().split())

G = [[] for i in range(N)]
G[X - 1].append(Y - 1)
G[Y - 1].append(X - 1)

for i in range(N - 1):
  G[i].append(i + 1)
  G[i + 1].append(i)
  
ans = [0 for i in range(N)]

from collections import deque
for st in range(N):
  q = deque([[st,0,-1]])
  visited = set()
  while q:
    v,dist,parent = q.popleft()
    if v in visited:
      continue
    visited.add(v)
    ans[dist] += 1
    for child in G[v]:
      if child == parent:
        continue
      q.append([child, dist + 1, v])
    
for i in range(1, N):
  print(ans[i] // 2)
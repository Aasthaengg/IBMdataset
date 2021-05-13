from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N, M, P = map(int,input().split())
es = []
to = defaultdict(list)
rto = defaultdict(list)
rf = [False]*N
rt = [False]*N
for i in range(M):
  a, b, c = map(int, input().split())
  es += [(a-1,b-1,-c+P)]
  to[a-1] += [b-1]
  rto[b-1] += [a-1]

def dfs(v):
  if rf[v]:
    return
  rf[v] = True
  for u in to[v]:
    dfs(u)

def rdfs(v):
  if rt[v]:
    return
  rt[v] = True
  for u in rto[v]:
    rdfs(u)

dfs(0)
rdfs(N-1)
ok = [False]*N
for i in range(N):
  ok[i] = rf[i]&rt[i]

dist = [float('inf')]*N
dist[0] = 0
upd = True
cnt = 0
while upd:
  upd = False
  for j in range(M):
    f, t, c = es[j]
    if (not ok[f]) or (not ok[t]):
      continue
    if dist[t]>dist[f]+c:
      upd = True
      dist[t] = dist[f]+c
  cnt += 1
  if cnt>N:
    print(-1)
    break
else:
  print(max(0,-dist[N-1]))
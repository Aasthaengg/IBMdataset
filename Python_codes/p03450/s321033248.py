from collections import deque
N, M, *L = map(int, open(0).read().split())
dic = [[] for i in range(N+1)]
llog = set()
rlog = set()
for l,r,d in zip(*[iter(L)]*3):
  dic[l].append((r,d))
  llog.add(l)
  rlog.add(r)
log = llog.difference(rlog)
q = deque(log)
dist = [-1]*(N+1)
for c in log:
  dist[c] = 0
while q:
  v = q.popleft()
  flag = False
  for u,d in dic[v]:
    if dist[u]==-1:
      dist[u] = dist[v]+d
      q.append(u)
    elif dist[u]!=dist[v]+d:
      print('No')
      flag = True
      break
  if flag:
    break
else:
  U = llog.union(rlog)
  for c in U:
    if dist[c]==-1:
      print('No')
      break
  else:
    print('Yes')
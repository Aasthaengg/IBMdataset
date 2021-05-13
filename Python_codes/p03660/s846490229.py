from collections import deque

def dfs(si, ei):
  q = deque()
  q.append([si,0])
  done = set([si])
  ds = [0 for _ in range(N)]
  while len(q) > 0:
    prvi, d = q.pop()
    for i in g[prvi]:
      if i in done: continue
      ds[i] = d+1
      q.append([i,d+1])
      done.add(i)
  return ds

N = int(input())
g = {i:[] for i in range(N)}
for _ in range(N-1):
  a,b = map(int,input().split())
  g[a-1].append(b-1)
  g[b-1].append(a-1)

dslist = dfs(0,N-1)
delist = dfs(N-1,0)

cntb, cntw = 0, 0
for ds, de in zip(dslist[1:N-1], delist[1:N-1]):
  if ds <= de: cntb += 1
  else: cntw += 1
print('Fennec' if cntb>cntw else 'Snuke')

from collections import deque
N, *L = map(int, open(0).read().split())
dic = [[] for i in range(N+1)]
for a,b in zip(*[iter(L)]*2):
  dic[a] += [b]
  dic[b] += [a]
fdist = [-1]*(N+1)
sdist = [-1]*(N+1)
fdist[1] = 0
sdist[N] = 0
q = deque([1])
while q:
  v = q.popleft()
  for u in dic[v]:
    if fdist[u] == -1:
      fdist[u] = fdist[v] + 1
      q.append(u)
q = deque([N])
while q:
  v = q.popleft()
  for u in dic[v]:
    if sdist[u]==-1:
      sdist[u] = sdist[v] + 1
      q.append(u)
ans = sum(a<=b for a,b in zip(fdist,sdist))-1
if 2*ans>N:
  print('Fennec')
else:
  print('Snuke')
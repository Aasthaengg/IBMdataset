from collections import defaultdict, deque
N, M = map(int, input().split())
used = [True]*N
dic = defaultdict(list)
for i in range(M):
  l, r, d = map(int,input().split())
  l -= 1
  r -= 1
  used[r] = False
  dic[l] += [(r,d)]

dist = [-1]*N
q = deque([])
for i in range(N):
  if used[i]:
    q += [i]
    dist[i] = 0

ans = True
while q:
  e = q.popleft()
  flag = False
  for p, d in dic[e]:
    if dist[p]==-1:
      dist[p] = d+dist[e]
      q += [p]
    elif dist[p]!=dist[e]+d:
      ans = False
      flag = True
      break
  if flag:
    break
if ans:
  if -1 not in dist:
    print('Yes')
  else:
    print('No')
else:
  print('No')
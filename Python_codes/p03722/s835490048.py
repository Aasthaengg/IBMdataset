from collections import defaultdict
N, M, *L = map(int, open(0).read().split())
dic = defaultdict(list)
rdic = defaultdict(list)
nin = [0]*N
Els = []
for a,b,c in zip(*[iter(L)]*3):
  dic[a-1] += [b-1]
  rdic[b-1] += [a-1]
  nin[b-1] += 1
  Els += [(a-1,b-1,c)]

To = [False]*N
From = [False]*N
q = [0]
To[0] = True
while q:
  p = q.pop()
  for e in dic[p]:
    if To[e]==False:
      To[e] = True
      q += [e]
q = [N-1]
From[N-1] = True
while q:
  p = q.pop()
  for e in rdic[p]:
    if From[e]==False:
      From[e] = True
      q += [e]

ok = [False]*N
for i  in range(N):
  ok[i] = To[i]&From[i]

cnt = 0
dist = [-float('inf')]*N
dist[0] = 0
cnt = 0
flag = False
while True:
  update = True
  for a,b,c in Els:
    if not(ok[a] and ok[b]):
      continue
    if dist[a]!=-float('inf') and dist[b]<dist[a]+c:
      dist[b] = dist[a]+c
      update = False
  if update:
    break
  cnt += 1
  if cnt>N:
    flag = True
    break

if flag:
  print('inf')
else:
  print(dist[N-1])
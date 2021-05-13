from collections import deque

n = int(input())
node = [[] for _ in range(n)]

for i in range(n-1):
  a, b = map(int, input().split())
  node[a-1].append(b-1)
  node[b-1].append(a-1)

not_yet = deque(node[0])
dist = [0]*n
par = [0]*n
for v in node[0]:
  dist[v] = 1
  par[v] = 0

while not_yet:
  key = not_yet.popleft()
  for v in node[key]:
    if dist[v] or v == 0:
      continue
    dist[v] = dist[key]+1
    par[v] = key
    not_yet.append(v)

k = n-1
for _ in range((dist[n-1]-1)//2):
  k = par[k]

ans = 0
not_yet = deque([])
already = [False]*n
already[0] = True
already[k] = True
already[n-1] = True
for v in node[0]:
  if already[v]:
    continue
  ans += 1
  not_yet.append(v)
  already[v] = True
while not_yet:
  key = not_yet.popleft()
  for v in node[key]:
    if already[v]:
      continue
    ans += 1
    not_yet.append(v)
    already[v] = True

judge = (n-2)//2+1
if ans >= judge:
  print("Fennec")
else:
  print("Snuke")
from collections import *
N = int(input())
G = [[] for n in range(N)]
for n in range(N-1):
  a,b = map(int,input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)

color = N*[0]
color[0] = 1
color[N-1] = -1
q = deque([])
q.append(0)
q.append(N-1)

while q:
  node = q.popleft()
  c = color[node]
  for to in G[node]:
    if color[to]==0:
      color[to] = c
      q.append(to)

b = color.count(1)
w = color.count(-1)

if w<b:
  print("Fennec")
else:
  print("Snuke")
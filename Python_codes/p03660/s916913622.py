from collections import deque

N = int(input())

G = [[] for _ in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
  
pars = [-1] * N
pars[0] = 0
stack = deque([0])
visited = [False] * N
visited[0] = True

while stack:
  now = stack.pop()
  for nxt in G[now]:
    if visited[nxt]:
      continue
    visited[nxt] = True
    pars[nxt] = now
    stack.append(nxt)

now = N-1
roads = []
while now != 0:
  now = pars[now]
  roads.append(now)

roads.reverse()
roads.append(N-1)
stack = deque([])
for i in range((len(roads)+1)//2):
  stack.append(roads[i])

stop = roads[(len(roads)+1)//2]
visited = [False] * N
for i in roads:
  visited[i] = True

black = (len(roads)+1)//2

while stack:
  now = stack.pop()
  for nxt in G[now]:
    if visited[nxt] or (nxt==stop):
      continue
    visited[nxt] = True
    stack.append(nxt)
    black += 1

white = N - black
if black > white:
  print('Fennec')
else:
  print('Snuke')
  


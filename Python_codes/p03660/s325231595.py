n = int(input())
g = [[] for _ in range(n)]
 
for i in range(n-1):
  a, b = map(int, input().split())
  a, b =  a-1, b-1
  g[a].append(b)
  g[b].append(a)

from collections import deque
f = deque()
s = deque()
 
f.append(0)
s.append(n-1)
 
f_visit = [-1]*n
s_visit = [-1]*n
f_visit[0] = 0
s_visit[n-1] = 0

def bfs(queue, visit):
  x = queue.popleft()
  for new_x in g[x]:
    if visit[new_x] == -1:
      visit[new_x] = visit[x]+1
      queue.append(new_x)
    else:
      continue

while f:
  bfs(f, f_visit)

while s:
  bfs(s, s_visit)

fp = 0
sp = 0
for i in range(n):
  if f_visit[i] <= s_visit[i]:
    fp += 1
  else:
    sp += 1
if fp <= sp:
  print('Snuke')
else:
  print('Fennec')
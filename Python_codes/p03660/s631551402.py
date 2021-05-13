from collections import deque
N = int(input())
g = [[] for i in range(N)]
for _ in range(N-1):
  a, b = map(int, input().split())
  g[b-1].append(a-1)
  g[a-1].append(b-1)
a = [-1]*N
b = [-1]*N
def bfs(n):
  q=deque()
  q.append(n)
  a[n] = 0
  while len(q):
    x=q.popleft()
    for i in g[x]:
      if a[i]==-1: 
        a[i]=a[x]+1
        q.append(i)
bfs(0)
def bfs2(n):
  q=deque()
  q.append(n)
  b[n] = 0
  while len(q):
    x=q.popleft()
    for i in g[x]:
      if b[i]==-1: 
        b[i]=b[x]+1
        q.append(i)
bfs2(N-1)
cnt = 0
for i in range(N):
  if a[i] <= b[i]:
    cnt += 1
  else:
    cnt -= 1
if cnt > 0:
  print('Fennec')
else:
  print('Snuke')
from collections import deque

n, m = map(int, input().split())
root = [[] for _ in range(n)]
adj = [-1 for _ in range(n)]
for _ in range(m):
  r,c = map(int, input().split())
  root[r-1].append(c-1)
  root[c-1].append(r-1)
  
explor = deque()
explor.append(0)

while explor:
  tmp = explor.popleft()
  for i in root[tmp]:
    if adj[i]==-1:
      adj[i] = tmp
      explor.append(i)

print('Yes')
for i in adj[1:]:
  print(i+1)
from collections import deque

n = int(input())
vdata = [list(map(int,input().split())) for _ in range(n)]
d = [-1]*n
q = deque()
q.append(vdata[0])
d[0] = 0

while len(q) > 0:
  node = q.popleft()
  c = d[node[0]-1]
  a = node[1]
  for i in range(a):
    b = node[i+2]-1
    if d[b] == -1:
      d[b] = c+1
      q.append(vdata[b])
      
for i in range(n):
  print(i+1, d[i])

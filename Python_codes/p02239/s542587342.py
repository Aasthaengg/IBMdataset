#coding: UTF-8
from collections import deque
n = int(input())
link = [[] for i in range(n+1)]
for i in range(n):
  r = list(map(int,input().split()))
  u = r.pop(0)
  k = r.pop(0)
  link[u] = r

searched=set()
queue = deque()
d = [-1 for i in range(n+1)]

v = 1
d[v] = 0
queue.append(v)
searched.add(v)
while queue:
  v = queue.popleft()
  for w in link[v]:
    if w not in searched:
      d[w] = d[v] + 1
      queue.append(w)
      searched.add(w)

for i in range(1,n+1):
  print(str(i) + " " + str(d[i]))


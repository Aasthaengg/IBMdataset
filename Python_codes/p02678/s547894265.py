from collections import deque
n,m = map(int,input().split())
graph = [[]for i in range(n+1)]

for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
#dist = [-1]*(n+1)
route = [-1]*(n+1)
route[0] = 0
route[0] = 0
#dist[0] = 0
#dist[1] = 0
d = deque()
d.append(1)
while d:
  v = d.popleft()
  for i in graph[v]:
    if route[i] == -1:
      #dist[i] = dist[v] + 1
      route[i] = v
      d.append(i)
if route.count(-1) == 0:
  print("Yes")
  for i in range(2,len(route)):
    print(route[i])
else:
  print("No")
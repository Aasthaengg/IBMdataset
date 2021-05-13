from collections import deque

N = int(input())
inf = 10 ** 6
graph = [[] for i in range(N)]
distance = [inf for i in range(N)]

for i in range(N):
  a = list(map(int,input().split()))
  a = list(map(lambda x: x - 1,a))
  k,n = a[0],a[1]
  if n >= 0:
    graph[k] = a[2:]
    

def bfs(path,root,dist):
  dist[root] = 0
  queue = deque([root])
  while queue:
    cur = queue.popleft()
    for chi in path[cur]:
      if dist[chi] == inf:
        queue.append(chi)
      dist[chi] = min(dist[cur] + 1,dist[chi])

bfs(graph,0,distance)
distance = [-1 if i == inf else i for i in distance]

for i,j in enumerate(distance):
  print(i + 1,j)
  

from collections import deque
q = deque([])
n = int(input())
G = []
for i in range(n):
  u, k, *vvv = list(map(int, input().split()))
  G.append([v-1 for v in vvv])
visited = [False for _ in range(n)]
q.append(0)
dist = [-1 for _ in range(n)]
dist[0] = 0
while q:
  u = q.popleft()
  visited[u] = True
  for v in G[u]:
    if visited[v] == True:
      continue
    else:
      q.append(v)
      visited[v] = True
      dist[v] = dist[u] + 1
    
for i in range(n):
  print(i+1, dist[i])
  

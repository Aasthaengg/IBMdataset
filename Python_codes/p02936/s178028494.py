from collections import deque

N, Q = map(int, input().split())
routings = [[] for _ in range(N+1)]

for _ in range(N-1):
  a, b = map(int, input().split())
  routings[a].append(b)
  routings[b].append(a)

points = [0 for _ in range(N+1)]
scores = [0 for _ in range(N+1)]

for _ in range(Q):
  p, x = map(int, input().split())
  points[p] += x

visited = [False for _ in range(N+1)]
  
edges = deque([1])
scores[1] = points[1]
visited[1] = True

while len(edges) > 0: 
  e = edges.pop()
  for c in routings[e]:
    if not visited[c]:
      scores[c] += scores[e] + points[c]
      visited[c] = True
      edges.append(c)
print(' '.join(map(str, scores[1:])))
  

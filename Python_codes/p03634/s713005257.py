from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
  a, b, c = map(int, input().split())
  G[a-1].append((b-1, c))
  G[b-1].append((a-1, c))
  
Q, K = map(int, input().split())
K -= 1
costs = [0] * N
stack = deque([K])
visited = [False]*N
visited[K] = True

while stack:
  now = stack.pop()
  for nxt, c in G[now]:
    if visited[nxt]:
      continue
    visited[nxt] = True
    costs[nxt] = costs[now] + c
    stack.append(nxt)
    
for i in range(Q):
  x, y = map(int, input().split())
  print(costs[x-1] + costs[y-1])
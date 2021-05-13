from collections import deque

n = int(input())
edge = [list(map(int, input().split())) for _ in range(n-1)]

adj = [[] for _ in range(n+1)]

for i in range(n-1):
    u, v, w = edge[i]
    adj[u].append([v, w])
    adj[v].append([u, w])

q = deque([1])

dist = [0] * (n+1)
visited = [False] * (n+1)

while len(q) > 0:
    v = q.popleft()
    for w, d in adj[v]:
        if not visited[w]:
            visited[w] = True
            dist[w] = dist[v] + d
            q.append(w)

#print(dist)

for i in range(1, n+1):
    if dist[i] % 2 == 0:
        print(0)
    else:
        print(1)
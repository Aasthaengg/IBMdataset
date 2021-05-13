from collections import deque

n = int(input())
to = [[] for _ in range(n)]

for i in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    to[a].append([b, c])
    to[b].append([a, c])

dist = [0 for _ in range(n)]
visited = [False for _ in range(n)]

def dfs(root):
    d = deque()
    d.append(root)
    while len(d) > 0:
        v = d.pop()
        visited[v] = True
        for u, c in to[v]:
            if visited[u]:
                continue
            d.append(u)
            dist[u] = dist[v]+c

q, k = map(int, input().split())
dfs(k-1)

for i in range(q):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    print(dist[x]+dist[y])
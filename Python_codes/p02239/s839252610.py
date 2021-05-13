from collections import deque

n = int(input())
g = [None] * n
visited = [0] * n
dist = [-1] * n
queue = deque()

while n:
    l = list(map(int, input().split()))
    connected = [i - 1 for i in l[2:]]
    g[l[0] - 1] = [i - 1 for i in l[2:]]
    n -= 1

queue.append((0, 0))
visited[0] = 1

while queue:
    i, d = queue.popleft()
    dist[i] = d
    for c in g[i]:
        if not visited[c]:
            visited[c] = 1
            queue.append((c, d + 1))

for i, d in enumerate(dist):
    print(i + 1, d)
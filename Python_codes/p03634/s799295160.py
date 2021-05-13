#jiriki-kibishi-katta
from collections import deque
n = int(input())
p = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    p[a].append((b, c))
    p[b].append((a, c))
q, k = map(int, input().split())
visited = [-1]*(n+1)
visited[k] = 0
queue = deque()
queue.append(k)
while len(queue):
    pos = queue.popleft()
    for nxt, w in p[pos]:
        if visited[nxt] != -1:
            continue
        visited[nxt] = visited[pos]+w
        queue.append(nxt)
for i in range(q):
    x, y = map(int, input().split())
    print(visited[x]+visited[y])
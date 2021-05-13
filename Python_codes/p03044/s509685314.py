from collections import deque
from collections import defaultdict

n = int(input())

graph = defaultdict(set)
visited = [1] * 2 + [0] * (n - 1)
ans = [0] * (n + 1)

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].add((v, w))
    graph[v].add((u, w))

q = deque([1])

while q:
    curr = q.popleft()
    visited[curr] = 1
    for v, w in graph[curr]:
        if not visited[v]:
            ans[v] = (ans[curr] + w) % 2
            q.append(v)
        else:
            continue

print(*ans[1:], sep="\n")
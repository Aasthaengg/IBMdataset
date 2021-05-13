import heapq
from collections import deque
n = int(input())
graph = [set() for _ in range(n)]

for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].add(b)
    graph[b].add(a)

nodes = [False for _ in range(n)]
values = list(map(lambda x: -int(x), input().split()))
print(-sum(values) + min(values))

heapq.heapify(values)
next_nodes = deque()
next_nodes.append(0)
while next_nodes:
    node = next_nodes.popleft()
    nodes[node] = -heapq.heappop(values)
    for g in graph[node]:
        if not (nodes[g]):
            next_nodes.append(g)

print(*nodes)
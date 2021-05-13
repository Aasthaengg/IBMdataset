from collections import deque

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))
q, k = map(int, input().split())

distance = [float('inf') for _ in range(n)]
distance[k - 1] = 0

d = deque()
d.append(k - 1)
visited = set({})
while d:
    point = d.popleft()
    for index, value in graph[point]:
        distance[index] = min(distance[point] + value, distance[index])
        if index not in visited:
            d.append(index)
    visited.add(point)
    
for _ in range(q):
    x, y = map(int, input().split())
    print(distance[x - 1] + distance[y - 1])
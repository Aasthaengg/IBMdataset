from collections import deque

N = int(input())

nodes = [tuple(map(int, input().split(' '))) for _ in range(N)]

distances = [-1] * (N + 1)

queue = deque()
queue.append((1, 0))

while len(queue) > 0:
    node, distance = queue.popleft()
    if distances[node] != -1:
        continue
    distances[node] = distance

    neighbors = nodes[node - 1][2:]
    for neighbor in neighbors:
        queue.append((neighbor, distance + 1))

for node in range(1, N + 1):
    print(node, distances[node])


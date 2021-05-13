import queue

n = int(input())
graph = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append([v - 1 for v in line[2:]])

q = queue.Queue()
q.put(0)
dist = [-1] * n
dist[0] = 0

while True:
    v = q.get()
    for next_v in graph[v]:
        if dist[next_v] == -1: 
            q.put(next_v)
            dist[next_v] = dist[v] + 1

    if q.empty():
        break

for i in range(n):
    print(i + 1, dist[i])


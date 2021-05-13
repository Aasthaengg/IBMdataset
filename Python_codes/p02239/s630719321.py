INF = float('inf')

v = int(input())
graph = [None]

for i in range(v):
    u = list(map(int, input().split()))
    
    graph.append(u[2:])

visited = [False] * (v+1)
visited[1] = True
cost = [INF] * (v+1)
cost[1] = 0
c = 0

q = graph[1]

while q:
    c += 1
    q_next = []
    for u in q:
        if not visited[u]:
            visited[u] = True
            cost[u] = c
            q_next.extend(graph[u])
    q = q_next
    
for i in range(v):
    if cost[i+1] == INF: cost[i+1] = -1
    print(i+1, cost[i+1])

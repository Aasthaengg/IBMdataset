import heapq
H, W = map(int, input().split())
edges = [[] for _ in range(10)]
for i in range(10):
    e_list = list(map(int, input().split()))
    for j in range(10):
        if j == i:
            continue
        edges[i].append([j, e_list[j]])
A = []
for i in range(H):
    A.append(list(map(int, input().split())))

def dijkstra(edges, num_v, start):
    dist = [float('inf')] * num_v
    dist[start] = 0
    q = []
    heapq.heappush(q, [0, start])

    while len(q) > 0:
        _, u = heapq.heappop(q)
        for edge in edges[u]:
            if dist[edge[0]] > dist[u] + edge[1]:
                dist[edge[0]] = dist[u] + edge[1]
                heapq.heappush(q, [dist[u] + edge[1], edge[0]])
    return dist
ans = 0
root_list = [0] * 10
for i in range(10):
    if i == 1:
        continue
    root_list[i] = dijkstra(edges, 10, i)[1]
for a_line in A:
    for a in a_line:
        if a == -1 or a == 1:
            continue
        ans += root_list[a]

print(ans)
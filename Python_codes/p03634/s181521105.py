import heapq
N = int(input())
edges = [[] for _ in range(N)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    edges[a-1].append([b-1, c])
    edges[b-1].append([a-1, c])
Q, K = map(int, input().split())
K -= 1


ans_list = []
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
base = dijkstra(edges,  N, K)
for i in range(Q):
    x, y = map(lambda n: int(n) - 1, input().split())
    x_K = base[x]
    K_y = base[y]
    ans_list.append(x_K + K_y)

for i in ans_list:
    print(i)
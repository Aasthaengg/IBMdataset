import networkx as nx

N = int(input())
UVW = [list(map(int, input().split())) for _ in range(N - 1)]

G = nx.Graph()

color = [0 for _ in range(N)]

for u, v, w in UVW:
    G.add_edge(u - 1, v - 1, weight=w)

color[0] = -1

pred, dist = nx.dijkstra_predecessor_and_distance(G, 0)

c = [dist[i] for i in range(N)]
ans = [1 if i % 2 == 0 else 0 for i in c]
print(*ans)

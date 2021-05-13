import collections
import heapq


class Dijkstra:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.neighbors = collections.defaultdict(list)

    def add_edge(self, x, y, d):
        self.neighbors[x].append((y, d))
        self.neighbors[y].append((x, d))

    def compute_all(self, s):
        distances = [float('inf') for _ in range(self.n_nodes)]
        visited = [False for _ in range(self.n_nodes)]
        prev_nodes = [None for _ in range(self.n_nodes)]
        distances[s] = 0
        q = []
        for t in range(self.n_nodes):
            heapq.heappush(q, (distances[t], t))
        while q:
            dist_x, x = heapq.heappop(q)
            if visited[x]:
                continue
            visited[x] = True

            for y, d_xy in self.neighbors[x]:
                if visited[y]:
                    continue
                dist_y = dist_x + d_xy
                if dist_y < distances[y]:
                    distances[y] = dist_y
                    prev_nodes[y] = x
                    heapq.heappush(q, (dist_y, y))
        return distances, prev_nodes


n = int(input())
dijkstra = Dijkstra(n)
for _ in range(n - 1):
    a, b = map(int, input().split())
    dijkstra.add_edge(a - 1, b - 1, 1)
ds0, _ = dijkstra.compute_all(0)
ds1, _ = dijkstra.compute_all(n - 1)
count = 0
for d0, d1 in zip(ds0, ds1):
    if d0 <= d1:
        count += 1
if count > n // 2:
    print('Fennec')
else:
    print('Snuke')
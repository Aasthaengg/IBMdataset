# https://atcoder.jp/contests/abc126/tasks/abc126_d

import heapq
from collections import defaultdict

class Dijkstra:
    def __init__(self, rote_map, start_point, goal_point=None):
        self.rote_map = rote_map
        self.start_point = start_point
        self.goal_point = goal_point

    def execute(self):
        num_of_city = len(self.rote_map)
        dist = [float("inf") for _ in range(num_of_city)]
        prev = [float("inf") for _ in range(num_of_city)]

        dist[self.start_point] = 0
        heap_q = []
        heapq.heappush(heap_q, (0, self.start_point))
        while len(heap_q) > 0:
            prev_cost, src = heapq.heappop(heap_q)

            if dist[src] < prev_cost:
                continue

            for dest, cost in self.rote_map[src].items():
                if cost != float("inf") and dist[dest] > dist[src] + cost:
                    dist[dest] = dist[src] + cost
                    heapq.heappush(heap_q, (dist[dest], dest))
                    prev[dest] = src
        return dist

    def get_path(self, goal, prev):
        path = [goal]
        dest = goal
        while prev[dest] != float("inf"):
            path.append(prev[dest])
            dest = prev[dest]
        return list(reversed(path))

n = int(input())
route_map = [dict() for _ in range(n)]
for i in range(n - 1):
    u, v, wi = map(int, input().split())
    u, v = u - 1, v - 1
    route_map[u][v] = wi
    route_map[v][u] = wi

d = Dijkstra(route_map, 0).execute()
for k in range(n):
    if d[k] % 2 == 0:
        print(0)
    else:
        print(1)
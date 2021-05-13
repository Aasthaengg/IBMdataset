import sys
sys.setrecursionlimit(10**6)

n, m, p = map(int, input().split())

edges = []
routes  = [[] for i in range(n)]
rev_routes = [[] for i in range(n)]
from_start = set()
to_goal = set()

def dfs(node, routes, seen):
    if node in seen:
        return
    seen.add(node)
    candidates = routes[node]
    for to in candidates:
        dfs(to, routes, seen)


for _ in range(m):
    node1, node2, value = map(int, input().split())
    node1, node2, value = node1-1, node2-1, value - p
    edges.append([node1, node2, value])
    routes[node1].append(node2)
    rev_routes[node2].append(node1)

dfs(0, routes, from_start)
dfs(n-1, rev_routes, to_goal)

from_start_to_goal = from_start & to_goal

graph = [-float('INF')] * n
graph[0] = 0

for i in range(n):
    is_updated = False
    for node, to, value in edges:
        if node not in from_start_to_goal or to not in from_start_to_goal:
            continue
        current_point = graph[node]
        next_point = graph[node] + value
        if graph[to] < next_point:
            graph[to] = next_point
            is_updated = True
        else:
            continue
    if not is_updated:
        score = max(0, graph[n-1])
        break
else:
    score = -1
      
print(score)

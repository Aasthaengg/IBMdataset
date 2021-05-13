import sys
sys.setrecursionlimit(10**6)

N = int(input())
paths = [dict() for i in range(N + 1)]
for i in range(N-1):
    u, v, w = map(int,input().split())
    paths[u][v] = w
    paths[v][u] = w

node_colors = [-1] * (N+1)

def route(last, now, dist):
    for next_node, next_distance in paths[now].items():
        node_colors[next_node] = (dist + next_distance) % 2
        if next_node != last:
            route(now, next_node, dist + next_distance)

node_colors[1] = 0

route(0, 1, 0)

for i in range(N):
    print(node_colors[i+1])

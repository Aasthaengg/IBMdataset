import sys

input = sys.stdin.buffer.readline

n, m, p = map(int, input().split())
graph = [[] for _ in range(n + 1)]
revgraph = [[] for _ in range(n + 1)]
loop = [False] * (n + 1)
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c - p))
    graph[a].append((b, c - p))
    revgraph[b].append((a, c - p))
is_route = [False] * (n + 1)
# DFS
start = 1

stack = [start]
while stack:
    v = stack.pop()
    is_route[v] = True
    for u, c in graph[v]:
        if is_route[u]:
            continue
        stack.append(u)
is_revroute = [False] * (n + 1)

goal = n
stack = [goal]
while stack:
    v = stack.pop()
    is_revroute[v] = True
    for u, c in revgraph[v]:
        if is_revroute[u]:
            continue
        stack.append(u)


def check(v):
    return is_route[v] and is_revroute[v]


# Bellman-Ford

dist = [-(10 ** 10)] * (n + 1)
start = 1
dist[start] = 0
cnt = 0
update = True
used = set([start])
while update:
    cnt += 1
    update = False
    for fr, to, co in edges:
        if check(fr) and check(to):
            if dist[fr] != -(10 ** 10) and dist[to] < dist[fr] + co:
                dist[to] = dist[fr] + co
                update = True
    if not update:
        break
    if cnt > n:
        print(-1)
        exit()
print(max(0, dist[n]) if dist[n] != -(10 ** 10) else -1)

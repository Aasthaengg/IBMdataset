from collections import deque
n, m, p = map(int, input().split())
graph = [[] for _ in range(n+1)]
edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    edge.append((a, b, -c+p))

q = deque([])
coins = [0] * (n+1)
ban = [False] * (n+1)

for i in range(1, n+1):
    q.append(i)
    time = [-1] * (n + 1)
    time[i] = 0
    while q:
        now = q.pop()
        for node, coin in graph[now]:
            if time[node] != -1:
                continue
            time[node] = time[now] + 1
            q.append(node)
    if i != 1:
        if time[n] == -1:
            ban[i] = True
    else:
        for j in range(2, n+1):
            if time[j] == -1:
                ban[j] = True


def bellman_ford(v, e_list, start, end):
    inf = 10**9
    dist = [inf] * (v+1)
    dist[start] = 0
    for j in range(v):
        for e in e_list:
            if ban[e[1]]:
                continue
            if dist[e[1]] > e[2] + dist[e[0]]:
                dist[e[1]] = e[2] + dist[e[0]]
                if j == v-1:
                    return -1, 0
    return dist[end], 1


ans, st = bellman_ford(n, edge, 1, n)
if st:
    print(max(-ans, 0))
else:
    print(-1)

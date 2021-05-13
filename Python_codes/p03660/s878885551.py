from collections import deque


def bfs(v, N):
    dist = [-1 for _ in range(N)]
    que = deque()
    que.append((v, 0, -1))
    while que:
        (now, cost, par) = que.popleft()
        dist[now] = cost
        for edge in edges[now]:
            if edge == par:
                continue
            que.append((edge, cost + 1, now))
    return dist


N = int(input())
edges = {i: [] for i in range(N)}
for _ in range(N - 1):
    a, b = map(int, input().split(' '))
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

dist_from_one = bfs(0, N)
dist_from_N = bfs(N - 1, N)
fennec = 0
for i in range(N):
    fennec += int(dist_from_one[i] <= dist_from_N[i])

print('Fennec' if 2 * fennec > N else 'Snuke')
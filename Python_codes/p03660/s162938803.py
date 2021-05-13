from collections import deque

N = int(input())
X = [list(map(int, input().split())) for _ in range(N - 1)]

edges = [[] for _ in range(N + 1)]
for u, v in X:
    edges[u].append(v)
    edges[v].append(u)


def bfs(s, x):
    inf = 10 ** 9 + 7
    d = [inf] * (N + 1)
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in edges[u]:
            if d[v] != inf:
                continue

            d[v] = d[u] + 1
            if v != x:
                q.append(v)

    return d


d1 = bfs(1, N)
d2 = bfs(N, 1)

cnt = 0
for i in range(1, N + 1):
    cnt += d1[i] <= d2[i]

if cnt > N // 2:
    print("Fennec")
else:
    print("Snuke")


from collections import deque

H, W = map(int, input().split())
X = [input() for _ in range(H)]


def bfs(si, sj):
    offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    INF = 10 ** 9 + 7
    d = [[INF] * W for _ in range(H)]
    d[si][sj] = 0 if X[si][sj] == "." else INF
    q = deque()
    q.append((si, sj))
    while q:
        u, v = q.popleft()
        for i, j in offset:
            if (0 <= u + i < H and 0 <= v + j < W and X[u + i][v + j] == "."
                    and d[u + i][v + j] > d[u][v] + 1):
                d[u + i][v + j] = d[u][v] + 1
                q.append((u + i, v + j))

    res = 0
    for x in d:
        for v in x:
            if v < INF:
                res = max(res, v)

    return res


ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, bfs(i, j))

print(ans)

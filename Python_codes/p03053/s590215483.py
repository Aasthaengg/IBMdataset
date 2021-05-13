from collections import deque


def bfs(q):
    ans = 0
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and dist[ni][nj] < 0:
                q.append((ni, nj))
                dist[ni][nj] = dist[i][j] + 1
                ans = max(ans, dist[ni][nj])
    return ans


H, W = map(int, input().split())
field = [input() for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
q = deque()
for i in range(H):
    for j in range(W):
        if field[i][j] == "#":
            dist[i][j] = 0
            q.append((i, j))
print(bfs(q))

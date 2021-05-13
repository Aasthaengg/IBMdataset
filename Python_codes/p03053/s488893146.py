from collections import deque, Counter


def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while que:
        p = que.popleft()
        y = p[0]
        x = p[1]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < H and 0 <= nx < W and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                que.append((ny, nx))
    return dist


# Input params and answer
H, W = map(int, input().split())
Map = [list(input()) for i in range(H)]
dist = [[-1] * W for i in range(H)]

# Initial Black Point
que = deque([])
for h in range(H):
    for w in range(W):
        if Map[h][w] == "#":
            que.append((h, w))
            dist[h][w] = 0

# BFS
nd = bfs()

ans = 0
for h in range(H):
    for w in range(W):
        if nd[h][w] > ans:
            ans = nd[h][w]

print(ans)

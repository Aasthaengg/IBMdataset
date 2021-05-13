from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

move = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[False] * W for _ in range(H)]


def bfs(i, j):
    b, w = 0, 0
    visited[i][j] = True
    que = deque([(i, j)])

    while que:
        ci, cj = que.popleft()
        if S[ci][cj] == '#':
            b += 1
        else:
            w += 1

        for di, dj in move:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < H and 0 <= nj < W) or visited[ni][nj]:
                continue
            if S[ci][cj] != S[ni][nj]:
                visited[ni][nj] = True
                que.append((ni, nj))

    return b * w


result = 0
for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        result += bfs(i, j)
print(result)

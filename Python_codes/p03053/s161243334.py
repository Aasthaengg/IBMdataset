from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

move = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[-1] * W for _ in range(H)]

ans = 0
que = deque([])
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            visited[i][j] = 0
            for di, dj in move:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W \
                   and S[ni][nj] != '#' and visited[ni][nj] == -1:
                    que.append((ni, nj, 1))
                    visited[ni][nj] = 1
                    ans = 1

while que:
    i, j, d = que.popleft()
    for di, dj in move:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == -1:
            que.append((ni, nj, d+1))
            visited[ni][nj] = d+1
            ans = d+1

print(ans)


from collections import deque
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
moves = ((1, 0), (0, 1), (0, -1), (-1, 0))

def bfs(sy, sx):
    q = deque([[sy, sx]])
    dist = [[float('inf')]*(W) for _ in range(H)]
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in moves:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W and s[ny][nx] == '.' and dist[ny][nx] == float('inf'):
                dist[ny][nx] = dist[y][x] + 1
                q += [[ny, nx]]

    return dist

d = bfs(0, 0)

if d[-1][-1] == float('inf'):
    print(-1)
    exit()

ans = H*W 
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            ans -= 1

ans -= d[-1][-1] + 1
print(ans)
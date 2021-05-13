from collections import deque
h, w = map(int, input().split())
map = [list(input()) for i in range(h)]
def bfs():
    d = [[float("inf")] * w for i in range(h)]
    sx = 0
    sy = 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    d[sx][sy] = 0
    que = deque([])
    que.append((sx, sy))
    while que:
        p = que.popleft()
        if p[0] == h-1 and p[1] == w-1:
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if 0 <= nx < h and 0 <= ny < w and map[nx][ny] != "#"\
            and d[nx][ny] == float("inf"):
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1
    return d[h-1][w-1]
count = 0
for i in range(h):
    for j in range(w):
        if map[i][j] == '#':
            count += 1
short = bfs()
if short == float("inf"):
    ans = -1
else:
    ans = h * w - count - short - 1
print(ans)           


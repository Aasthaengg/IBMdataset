from collections import deque

tx = [1, 0, -1, 0]
ty = [0, 1, 0, -1]

H, W = map(int,input().split())

MAP = []

for _ in range(H):
    MAP.append(list(input()))

d = deque()

for i in range(H):
    for j in range(W):
        if MAP[i][j] == '#':
            d.append([i, j, 0])

ans = 0

while len(d) != 0:
    x, y, cnt = d.popleft()
    for i in range(4):
        nx = x + tx[i]
        ny = y + ty[i]
        if 0 <= nx < H and 0 <= ny < W and MAP[nx][ny] == '.':
            MAP[nx][ny] = '#'
            d.append([nx, ny, cnt + 1])
            ans = max(ans, cnt + 1)

print(ans)
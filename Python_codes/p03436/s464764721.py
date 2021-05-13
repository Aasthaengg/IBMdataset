from collections import deque

H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

cnt_white = 0
for path in field:
    cnt_white += path.count('.')

sy, sx = 0, 0
gy, gx = H - 1, W - 1

dyx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()
q.append((sy, sx, 0))

while q:
    cy, cx, ct = q.popleft()
    for dy, dx in dyx:
        ny, nx = cy + dy, cx + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if (ny, nx) == (gy, gx):
            print(cnt_white - (ct + 2)) # ct + 2 が使用した '.' の個数
            exit()
        if field[ny][nx] == '#':
            continue
        q.append((ny, nx, ct + 1))
        field[ny][nx] = '#'

print('-1')
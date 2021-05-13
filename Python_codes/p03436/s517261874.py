from collections import deque

h, w = map(int, input().split())

s = [[] for _ in range(h)]
dis = [[-1] * w for _ in range(h)]

for i in range(h):
    s[i] = input()

white_cnt = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            white_cnt += 1

q = deque()
q.append([0, 0, 1])  # x,y,d
dis[0][0] = 1

while len(q) > 0:
    x, y, d = q.popleft()
    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 > nx or w <= nx or 0 > ny or h <= ny:
            continue
        if dis[ny][nx] != -1 or s[ny][nx] == "#":
            continue
        q.append([nx, ny, d + 1])
        dis[ny][nx] = d + 1

if dis[h - 1][w - 1] == -1:
    print(-1)
else:
    print(white_cnt - dis[h - 1][w - 1])


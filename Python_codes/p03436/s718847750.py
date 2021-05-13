h, w = map(int, input().split())
s = [[0 if c == '#' else 1 for c in input()] for _ in range(h)]

directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
dist = [[-1 for _ in range(w)] for _ in range(h)]
dist[0][0] = 0
q = [(0, 0)]
for y, x in q:
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if (ny < 0 or h <= ny) or (nx < 0 or w <= nx):
            continue
        if not s[ny][nx]:
            continue
        if dist[ny][nx] >= 0:
            continue
        dist[ny][nx] = dist[y][x] + 1
        q.append((ny, nx))

if dist[-1][-1] < 0:
    print(-1)
else:
    print(sum(sum(si) for si in s) - dist[-1][-1] - 1)
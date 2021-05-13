import collections

H, W = map(int, input().split())
s = [input() for _ in range(H)]

sy, sx = 0, 0
gy, gx = H - 1, W - 1

dist = [[-1 for _ in range(W)] for _ in range(H)]

q = collections.deque()
q.append((sy, sx, 0))

while q:
    y, x, d = q.popleft()

    if y < 0 or H <= y or x < 0 or W <= x:
        continue

    if s[y][x] == '#':
        continue

    if dist[y][x] != -1:
        continue

    dist[y][x] = d + 1

    q.append((y + 1, x, d + 1))
    q.append((y - 1, x, d + 1))
    q.append((y, x + 1, d + 1))
    q.append((y, x - 1, d + 1))

if dist[-1][-1] == -1:
    print(-1)
else:
    num_white = sum(block == '.' for row in s for block in row)
    print(num_white - dist[-1][-1])

from collections import deque
h, w = map(int, input().split())
a = [input() for _ in range(h)]
inf = 10 ** 7

d = [[inf for _ in range(w)] for _ in range(h)]
que = deque()

for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            que.append((i, j))
            d[i][j] = 0

while que:
    px, py = que.popleft()
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        qx, qy = px + dx, py + dy
        if 0 <= qx < h and 0 <= qy < w:
            if d[qx][qy] > d[px][py] + 1:
                d[qx][qy] = d[px][py] + 1
                que.append((qx, qy))

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, d[i][j])

print(ans)
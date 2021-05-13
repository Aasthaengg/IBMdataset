from collections import deque

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

h, w = map(int, input().split())
table = []
for _ in range(h):
    table.append(list(input()))
q = deque()
for y in range(h):
    for x in range(w):
        if table[y][x] == "#":
            q.append((y, x))
            table[y][x] = 0

while q:
    y, x = q.popleft()
    d = table[y][x]
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < h and 0 <= nx < w:
            if table[ny][nx] == ".":
                table[ny][nx] = d + 1
                q.append((ny, nx))
print(max(list(map(lambda n: max(n), table))))

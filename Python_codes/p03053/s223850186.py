from collections import deque

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

q = deque([])
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            q.append([i, j])
            q.append(0)

while q:
    y, x = q.popleft()
    ans = q.popleft() + 1
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ny, nx = dy + y, dx + x
        if ny < 0 or nx < 0 or ny >= h or nx >= w:
            continue
        if a[ny][nx] == '.':
            a[ny][nx] = '#'
            q.append([ny, nx])
            q.append(ans)

print(ans-1)
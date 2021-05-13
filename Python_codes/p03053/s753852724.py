from collections import deque

H, W = map(int, input().split())
s_l = [input() for _ in range(H)]
dist = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = deque()
results = []
for y, s in enumerate(s_l):
    result = []
    for x, p in enumerate(s):
        result.append(False if p == "." else True)
        if p == "#":
            queue.append((y, x))
    results.append(result)

count = 0
while queue:
    starts = []
    while queue:
        starts.append(queue.popleft())
    for y, x in starts:
        for dy, dx in dist:
            ny = y + dy
            nx = x + dx
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if s_l[ny][nx] == "." and not results[ny][nx]:
                queue.append((ny, nx))
                results[ny][nx] = True
    if queue:
        count += 1

print(count)

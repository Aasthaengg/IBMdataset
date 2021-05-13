from collections import deque
from itertools import product

H, W = map(int, input().split(' '))
maze = [input() for _ in range(H)]

points = [(y, x) for y, x in product(range(H), range(W)) if maze[y][x] == '.']

ans = 0
for sy, sx in points:
    costs = {}
    queue = deque()
    queue.append((sy, sx, 0))
    while queue:
        y, x, cost = queue.popleft()
        if (y, x) in costs:
            continue
        else:
            costs[(y, x)] = cost

        for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if not 0 <= ny < H:
                continue
            if not 0 <= nx < W:
                continue
            if (ny, nx) in costs:
                continue
            if maze[ny][nx] == '#':
                continue
            queue.append((ny, nx, cost + 1))

    ans = max(ans, max(costs.values()))

print(ans)

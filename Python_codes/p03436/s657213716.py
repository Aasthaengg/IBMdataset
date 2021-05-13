from collections import deque
h, w = map(int, input().split())
ss = [input() for _ in range(h)]
q = deque([(0, 0, 0)])
cost = 0
visited = [[False for _ in range(w)] for _ in range(h)]


def find():
    while len(q) > 0:
        y, x, cost = q.popleft()
        if (y, x) == (h - 1, w - 1):
            return cost
        if 0 <= y < h and 0 <= x < w and ss[y][x] != '#' and not visited[y][x]:
            visited[y][x] = True
            q.append((y + 1, x, cost + 1))
            q.append((y - 1, x, cost + 1))
            q.append((y, x + 1, cost + 1))
            q.append((y, x - 1, cost + 1))
    return -1


c = find()
if c < 0:
    print(-1)
else:
    dots = 0
    for i in range(h):
        for j in range(w):
            if ss[i][j] != '#':
                dots += 1
    print(dots - c - 1)

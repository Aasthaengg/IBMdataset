from collections import deque
h, w = map(int, input().split())
wall = '#'
maze = [[wall] * (w + 2)]
wn = 0
for y in range(1, h+1):
    maze.append([wall] + [c for c in input()] + [wall])
    for x in range(1, w+1):
        if maze[y][x] == '.':
            wn += 1
maze.append([wall] * (w + 2))

q = deque()
q.append((1, 1, 0))
reachable = False
while q:
    y, x, i = q.popleft()
    if maze[y][x] == '#':
        continue
    if y == h and x == w:
        reachable = True
        break
    maze[y][x] = '#'
    i += 1
    q.append((y+1, x, i))
    q.append((y-1, x, i))
    q.append((y, x+1, i))
    q.append((y, x-1, i))
print(wn - i - 1 if reachable else -1)

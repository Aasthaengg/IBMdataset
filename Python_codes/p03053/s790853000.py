from collections import deque
h, w = map(int, input().split())
wall = '/'
grid = [[wall] * (w + 2)]
wn = 0

q = deque()
for y in range(1, h+1):
    grid.append([wall] + [c for c in input()] + [wall])
    for x in range(1, w+1):
        if grid[y][x] == '.':
            wn += 1
        if grid[y][x] == '#':
            q.append((y, x, 0))
grid.append([wall] * (w + 2))

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    y, x, i = q.popleft()
    grid[y][x] = '#'
    for dy, dx in move:
        if grid[y + dy][x + dx] == '.':
            grid[y + dy][x + dx] = '#'
            q.append((y + dy, x + dx, i + 1))
    
print(i)

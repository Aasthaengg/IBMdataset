from itertools import product

direction = []
for i in range(4):
    dx = 5 % (i + 1) - 1
    dy = 5 % (i + 2) - 1
    direction.append((dx, dy))
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
visited = [[False for _ in range(W)] for _ in range(H)]
ans = 0
for i, j in product(range(H), range(W)):
    if visited[i][j]: continue
    stack = [(i, j)]
    black = 0; white = 0;
    while stack:
        x, y = stack.pop()
        if visited[x][y]: continue
        visited[x][y] = True
        if grid[x][y] == '#': black += 1
        else: white += 1
        for dx, dy in direction:
            temp_x, temp_y = min(max(x + dx, 0), H-1), min(max(y + dy, 0), W-1)
            if visited[temp_x][temp_y]: continue
            if grid[x][y] != grid[temp_x][temp_y]: stack.append((temp_x, temp_y))
    ans += black * white
print(ans)
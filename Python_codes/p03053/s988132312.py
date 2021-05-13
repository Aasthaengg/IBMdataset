from collections import deque
def gridbfs(grid):
    INF = 10**18

    gridy = len(grid)
    gridx = len(grid[0])

    dist = [[INF]*gridx for _ in range(gridy)]
    q = deque()
    for y in range(gridy):
        for x in range(gridx):
            if grid[y][x] == '#':
                dist[y][x] = 0
                q.append((y,x))

    while q:
        y,x = q.popleft()
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny,nx = y+dy, x+dx
            if not (0 <= ny < gridy and 0 <= nx < gridx):
                continue
            if dist[ny][nx] != INF:
                continue
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny,nx))

    return dist

H,W = map(int,input().split())
Grid = [input() for _ in range(H)]
d = gridbfs(Grid)
print(max(max(d[i]) for i in range(H)))

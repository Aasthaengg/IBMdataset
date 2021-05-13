H, W = map(int, input().split())
maze = [input() for _ in range(H)]
seen = [[-1] * W for _ in range(H)]

from collections import deque


queue = deque()
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            queue.append([i, j, 0])
            seen[i][j] = 0

def bfs(maze, seen):
    while queue:
        y, x, c = queue.popleft()
        for i, j in [1, 0], [-1, 0], [0, 1], [0, -1]:
            dy = y + i
            dx = x + j
            if dy < 0 or H <= dy or dx < 0 or W <= dx:
                continue
            if seen[dy][dx] > -1:
                continue
            if maze[dy][dx] == '#':
                continue
            seen[dy][dx] = c + 1
            queue.append([dy, dx, c+1])

def check_max(seen):
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, seen[i][j])
    return ans
    
bfs(maze, seen)
print(check_max(seen))
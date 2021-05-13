from collections import deque
H, W = map(int, input().split())
maze = [input() for i in range(H)]

def bfs(maze, sy, sx):
    visited = [[-1]*W for j in range(H)]
    queue = deque([[sy, sx]])
    visited[sy][sx] = 0
    while queue:
        ans=0
        y, x = queue.popleft()
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_y, new_x = y+j, x+k
            if 0 <= new_y < H and 0 <= new_x < W:
                if maze[new_y][new_x] == "." and visited[new_y][new_x] == -1 :
                    visited[new_y][new_x] = visited[y][x] + 1
                    queue.append([new_y, new_x])
                    
    for l in range(H):
        for m in range(W):
            ans = max(ans,visited[l][m])
            
    return ans
        
ma=0
for sy in range(H):
    for sx in range(W):
        if maze[sy][sx] == ".":
            if bfs(maze,sy,sx) is not None:
                ma = max(bfs(maze, sy, sx),ma)
print(ma)

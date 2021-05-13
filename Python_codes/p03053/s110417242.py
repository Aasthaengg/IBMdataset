from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

def BFS(H, W, grid):
    visited = [[True for _ in range(W+2)] for _ in range(H+2)]
    que = deque()
    for i in range(H):
        visited[i+1][1:-1] = map(lambda _:_=="#", grid[i])
        for j in range(W):
            if(grid[i][j] == "#"):
                que.append((i+1, j+1, 0))
    dist = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        
    while que:
        x, y, c = que.popleft()
        for dx, dy in dist:
            nx = x + dx
            ny = y + dy
            
            if(not visited[nx][ny]):
                que.append((nx, ny, c+1))
                visited[nx][ny] = True
    return c
        
print(BFS(H, W, grid))
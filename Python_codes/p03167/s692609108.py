def grid(maze,h,w):
    mod = 7+10**9
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maze[i][j] == "#":
                continue

            if i==0 and j==0:
                visited[i][j] = 1
                
            
            elif i == 0:
                visited[i][j] = visited[i][j-1]
            elif j == 0:
                visited[i][j] = visited[i-1][j]
            else:
                visited[i][j] = (visited[i-1][j]%mod + visited[i][j-1]%mod)%mod
    
    return visited[h-1][w-1]


h,w = map(int,input().split())

maze = []

for _ in range(h):
    maze.append(list(input()))

print(grid(maze,h,w))

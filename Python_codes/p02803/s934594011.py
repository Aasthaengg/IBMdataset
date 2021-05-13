from collections import deque
h,w = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0
maze = []
for i in range(h):
    maze.append(list(input()))
for i in range(h):
    for j in range(w):
        if maze[i][j] == ".":
            d = [[-1 for a in range(w)] for b in range(h)]
            dq = deque([(j,i)])
            d[i][j] = 0
            while dq:
                x,y = dq.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<=w-1 and 0<=ny<=h-1 and maze[ny][nx] != "#" and d[ny][nx] == -1:
                        dq.append((nx,ny))
                        d[ny][nx] = d[y][x]+1
                        ans = max(ans,d[ny][nx])
print(ans)
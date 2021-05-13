from collections import deque
import copy
h,w = map(int,input().split())
origin = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0
for i in range(h):
    origin.append(list(input()))
for i in range(h):
    if "#" in origin[i]:
        break
else:
    print(h+w-2)
    exit()
for i in range(h):
    for j in range(w):
        if origin[i][j] == ".":
            d = [[0 for j in range(w)] for i in range(h)]
            maze = copy.deepcopy(origin)
            dq = deque([(j,i)])
            while dq:
                x,y = dq.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<=w-1 and 0<=ny<=h-1 and maze[ny][nx] != "#":
                        dq.append((nx,ny))
                        d[ny][nx] = d[y][x]+1
                        ans = max(ans,d[ny][nx])
                maze[y][x] = "#"
            #print(maze)
print(ans)
import sys
h,w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i,row in enumerate(grid):
    for j in range(w):
        if grid[i][j] == "#":
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]            
                if (nx < 0) or (w-1 < nx) or (ny < 0) or (h-1 < ny):
                    continue
                elif grid[ny][nx] == "#":
                    break
                else:
                    pass
            else:
                print("No")
                sys.exit()
else:
    print("Yes")
h,w = map(int,input().split())
grid = []
grid.append(["."]*(w+2))
for i in range(h):
    grid.append(["."]+list(input())+["."])
grid.append(["."]*(w+2))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(1,h+1):
    for j in range(1,w+1):
        if grid[i][j] == "#":
            ok = False
            for k in range(4):
                if grid[i+dy[k]][j+dx[k]] == "#":
                    ok = True
            if not ok:
                print("No")
                exit()
print("Yes")
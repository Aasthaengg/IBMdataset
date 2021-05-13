h, w = map(int,input().split())

grid = []
for _ in range(h):
    grid.append(list(input()))

dx=[-1,0,0,1]
dy=[0,-1,1,0]


for i in range(h):
    for j in range(w):
        flag=False
        if grid[i][j]==".":
            continue

        for x,y in zip(dx,dy):
            if i+x<0 or i+x>h-1 or j+y<0 or j+y>w-1:
                continue
            if grid[i+x][j+y]=="#":
                flag=True
                break

        if not flag:
            print("No")
            exit()

print("Yes")

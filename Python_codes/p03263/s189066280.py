h,w = map(int,input().split())
grid = []
ans = []
for i in range(h):
    grid.append(list(map(int,input().split())))
cur = [0,0]
while True:
    y,x = cur[0],cur[1]
    if y % 2 == 0:
        if x != w-1:
            if grid[y][x] % 2 == 1:
                grid[y][x] -= 1
                grid[y][x+1] += 1
                ans.append((y+1,x+1,y+1,x+2))
            cur[1] += 1
        else:
            if y >= h-1:
                break
            if grid[y][x] % 2 == 1:
                grid[y][x] -= 1
                grid[y+1][x] += 1
                ans.append((y+1,x+1,y+2,x+1))
            cur[0] += 1
    else:
        if x != 0:
            if grid[y][x] % 2 == 1:
                grid[y][x] -= 1
                grid[y][x-1] += 1
                ans.append((y+1,x+1,y+1,x))
            cur[1] -= 1
        else:
            if y >= h-1:
                break
            if grid[y][x] % 2 == 1:
                grid[y][x] -= 1
                grid[y+1][x] += 1
                ans.append((y+1,x+1,y+2,x+1))
            cur[0] += 1
print(len(ans))
for i in ans:
    print(i[0],i[1],i[2],i[3])
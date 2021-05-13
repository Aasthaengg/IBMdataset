import copy
H,W,n_black = map(int,input().split())
grid = [list(input()) for _ in range(H)]
for y in range(H):
    for x in range(W):
        if grid[y][x] == "#":
            grid[y][x] = 1
        else:
            grid[y][x] = 0
num_pat = 2**(H+W)
ans = 0
for i in range(num_pat):
    now_grid = copy.deepcopy(grid)
    for j in range(H+W):    
        if i>>j & 1:
            if j < H:
                for x in range(W):
                    now_grid[j][x] = 0
            else:
                j -= H
                for y in range(H):
                    now_grid[y][j] = 0
    black = 0
    for y in range(H):
        black += sum(now_grid[y])
    if black == n_black:
        ans += 1
print(ans)


    
    

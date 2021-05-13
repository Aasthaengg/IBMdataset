H, W = map(int, input().split())
grid = []
for _ in range(H):
    grid.append([s for s in input()])
    
left = [[0 for _ in range(W)] for _ in range(H)]
right = [[0 for _ in range(W)] for _ in range(H)]
up = [[0 for _ in range(W)] for _ in range(H)]
down = [[0 for _ in range(W)] for _ in range(H)]

for h in range(H):
    for w in range(W):
        if grid[h][w] == ".":
            if w == 0:
                left[h][w] = 1
            else:
                left[h][w] += left[h][w - 1] + 1

for h in range(H):
    for w in range(W)[::-1]:
        if grid[h][w] == ".":
            if w == W - 1:
                right[h][w] = 1
            else:
                right[h][w] += right[h][w + 1] + 1
            
for w in range(W):
    for h in range(H):
        if grid[h][w] == ".":
            if h == 0:
                up[h][w] = 1
            else:
                up[h][w] += up[h - 1][w] + 1
                
for w in range(W):
    for h in range(H)[::-1]:
        if grid[h][w] == ".":
            if h == H - 1:
                down[h][w] = 1
            else:
                down[h][w] += down[h + 1][w] + 1
                
ans = -10000
for h in range(H):
    for w in range(W):
        ans = max(ans, up[h][w] + down[h][w] + right[h][w] + left[h][w] - 3)
print(ans)
h,w = map(int,input().split())
grid = []
for i in range(h):
    grid.append(list(map(int,input().split())))
ans = []
for i in range(h):
    for j in range(w):
        if j == w-1:
            if grid[i][j] % 2 == 1 and i != h-1:
                grid[i+1][j] += 1
                ans.append([i+1,j+1,i+2,j+1])
        elif grid[i][j] % 2 == 1:
            grid[i][j+1] += 1
            ans.append([i+1,j+1,i+1,j+2])
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])




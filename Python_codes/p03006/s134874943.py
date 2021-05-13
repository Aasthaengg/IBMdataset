n = int(input())
grid = []
if n == 1:
    print(1)
    exit()
for _ in range(n):
    x,y = map(int,input().split())
    grid.append((x,y))
S = set(grid)
ans = float("inf")
for i in range(n-1):
    for j in range(i+1,n):
        cnt = 0
        p = grid[i][0]-grid[j][0]
        q = grid[i][1]-grid[j][1]
        for k in range(n):
            if (grid[k][0]-p,grid[k][1]-q) in S:
                cnt += 1
        else:
            ans = min(n-cnt,ans)
print(ans)
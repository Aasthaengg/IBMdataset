R,C,K = map(int,input().split())

grid=[[0]*C for _ in range(R)]
for i in range(K):
    x,y,v = map(int,input().split())
    grid[x-1][y-1] = v


dp0 = [[0]*(C+1) for _ in range(R+1)]
dp1 = [[0]*(C+1) for _ in range(R+1)]
dp2 = [[0]*(C+1) for _ in range(R+1)]
dp3 = [[0]*(C+1) for _ in range(R+1)]

for i in range(R):
    for j in range(C):
        dp1[i][j] = max(dp1[i][j-1],dp1[i-1][j]+grid[i][j],
                    dp2[i-1][j]+grid[i][j],dp3[i-1][j]+grid[i][j])
        dp2[i][j] = max(dp2[i][j-1],dp1[i][j-1]+grid[i][j])
        dp3[i][j] = max(dp3[i][j-1],dp2[i][j-1]+grid[i][j])
ans=max(dp1[R-1][C-1],dp2[R-1][C-1],dp3[R-1][C-1])
print(ans)
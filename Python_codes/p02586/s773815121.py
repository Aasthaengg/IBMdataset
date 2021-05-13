R , C , K = map(int,input().split())
masu = [[0 for i in range(C)] for j in range(R)]
for i in range(K):
    r , c , v = map(int,input().split())
    masu[r-1][c-1] = v

dp0 = [[0 for i in range(C)] for j in range(R)]
dp1 = [[0 for i in range(C)] for j in range(R)]
dp2 = [[0 for i in range(C)] for j in range(R)] 
dp3 = [[0 for i in range(C)] for j in range(R)]

if masu[0][0] != 0:
    dp1[0][0] = masu[0][0]
for i in range(1,C):
    dp0[0][i] = max(dp0[0][i],dp0[0][i-1])
    dp1[0][i] = max(dp1[0][i],dp1[0][i-1])
    dp2[0][i] = max(dp2[0][i],dp2[0][i-1])
    dp3[0][i] = max(dp3[0][i],dp3[0][i-1])
    if masu[0][i] != 0:
        dp3[0][i] = max(dp3[0][i],dp2[0][i]+masu[0][i])
        dp2[0][i] = max(dp2[0][i],dp1[0][i]+masu[0][i])
        dp1[0][i] = max(dp1[0][i],dp0[0][i]+masu[0][i])




for i in range(1,R):
    for j in range(C):
        dp0[i][j] = max(dp0[i][j],dp0[i-1][j],dp1[i-1][j],dp2[i-1][j],dp3[i-1][j])
        if j != 0:
            dp0[i][j] = max(dp0[i][j],dp0[i][j-1])
            dp1[i][j] = max(dp1[i][j],dp1[i][j-1])
            dp2[i][j] = max(dp2[i][j],dp2[i][j-1])
            dp3[i][j] = max(dp3[i][j],dp3[i][j-1])
        if masu[i][j] != 0:
            dp3[i][j] = max(dp3[i][j],dp2[i][j]+masu[i][j])
            dp2[i][j] = max(dp2[i][j],dp1[i][j]+masu[i][j])
            dp1[i][j] = max(dp1[i][j],dp0[i][j]+masu[i][j])
print(max(dp0[-1][-1],dp1[-1][-1],dp2[-1][-1],dp3[-1][-1]))
R,C,K = map(int, input().split())
L = [[0]*C for _ in range(R)]
for _ in range(K):
    r,c,v = map(int, input().split())
    L[r-1][c-1] = v

dp0 = [[0]*C for _ in range(R)]
dp1 = [[0]*C for _ in range(R)]
dp2 = [[0]*C for _ in range(R)]
dp3 = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if i == 0 and j == 0 and L[i][j] > 0:
            dp1[i][j] = L[i][j]
        elif i == 0:
            dp0[i][j] = dp0[i][j-1]
            dp1[i][j] = dp1[i][j-1]
            dp2[i][j] = dp2[i][j-1]
            dp3[i][j] = dp3[i][j-1]
            if L[i][j] > 0:
                dp1[i][j] = max(dp1[i][j], dp0[i][j-1]+L[i][j])
                dp2[i][j] = max(dp2[i][j], dp1[i][j-1]+L[i][j])
                dp3[i][j] = max(dp3[i][j], dp2[i][j-1]+L[i][j])
        elif j == 0:
            dp0[i][j] = max(dp0[i-1][j], dp1[i-1][j], dp2[i-1][j], dp3[i-1][j])
            if L[i][j] > 0:
                dp1[i][j] = dp0[i][j]+L[i][j]
        else:
            dp0[i][j] = max(dp0[i-1][j], dp1[i-1][j], dp2[i-1][j], dp3[i-1][j], dp0[i][j-1])
            dp1[i][j] = dp1[i][j-1]
            dp2[i][j] = dp2[i][j-1]
            dp3[i][j] = dp3[i][j-1]
            if L[i][j] > 0:
                dp1[i][j] = max(dp1[i][j], dp0[i][j]+L[i][j])
                dp2[i][j] = max(dp2[i][j], dp1[i][j-1]+L[i][j])
                dp3[i][j] = max(dp3[i][j], dp2[i][j-1]+L[i][j])

print(max(dp0[-1][-1], dp1[-1][-1], dp2[-1][-1], dp3[-1][-1]))
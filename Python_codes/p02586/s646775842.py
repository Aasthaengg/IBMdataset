R, C, K = map(int, input().split())

I = [[0]*C for i in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    I[r-1][c-1] = v   # 0-indexed

dp0 = [[0 for j in range(C+1)] for i in range(R+1)]
dp1 = [[0 for j in range(C+1)] for i in range(R+1)]
dp2 = [[0 for j in range(C+1)] for i in range(R+1)]
dp3 = [[0 for j in range(C+1)] for i in range(R+1)]
for i in range(R):
    for j in range(C):
        dp3[i][j] = max(dp3[i][j], dp2[i][j]+I[i][j])
        dp2[i][j] = max(dp2[i][j], dp1[i][j]+I[i][j])
        dp1[i][j] = max(dp1[i][j], dp0[i][j]+I[i][j])
        dp0[i+1][j] = max(dp0[i+1][j], dp0[i][j], dp1[i]
                          [j], dp2[i][j], dp3[i][j])
        dp0[i][j+1] = max(dp0[i][j+1], dp0[i][j])
        dp1[i][j+1] = max(dp1[i][j+1], dp1[i][j])
        dp2[i][j+1] = max(dp2[i][j+1], dp2[i][j])
        dp3[i][j+1] = max(dp3[i][j+1], dp3[i][j])


# print(*dp, sep=' \n')

ans = max(dp0[R-1][C-1], dp1[R-1][C-1], dp2[R-1][C-1], dp3[R-1][C-1])
print(ans)

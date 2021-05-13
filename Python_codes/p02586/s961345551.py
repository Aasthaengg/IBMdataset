r,c,k = map(int,input().split())
t = [[0 for i in range(c)] for i in range(r)]
for i in range(k):
    a,b,z = map(int,input().split())
    t[a-1][b-1] = z
dp = [[[0 for i in range(c)]for i in range(r)]for i in range(4)]
dp[0][0][0] = 0
dp[1][0][0] = t[0][0]
dp[2][0][0] = t[0][0]
dp[3][0][0] = t[0][0]
for i in range(r-1):
    dp[0][i+1][0] = dp[1][i][0]
    for j in range(1,4):
        dp[j][i+1][0] = dp[1][i][0]+t[i+1][0]
for i in range(c-1):
    dp[0][0][i+1] = 0
    for j in range(1,4):
        dp[j][0][i+1] = max(dp[1][0][i],t[0][i+1])
    for j in range(2,4):
        dp[j][0][i+1] = max(dp[2][0][i],dp[1][0][i]+t[0][i+1])
    dp[3][0][i+1] = max(dp[3][0][i],dp[2][0][i]+t[0][i+1])
for i in range(r-1):
    for j in range(c-1):
        u = max(dp[0][i+1][j],dp[3][i][j+1])
        for s in range(0,4):
            dp[s][i+1][j+1] =  u
        u = max(dp[0][i+1][j]+t[i+1][j+1],dp[1][i+1][j],dp[3][i][j+1]+t[i+1][j+1])
        for s in range(1,4):
            dp[s][i+1][j+1] = u
        u = max(dp[1][i+1][j]+t[i+1][j+1],dp[2][i+1][j],dp[3][i][j+1]+t[i+1][j+1])
        for s in range(2,4):
            dp[s][i+1][j+1] = u
        dp[3][i+1][j+1] = max(dp[2][i+1][j]+t[i+1][j+1],dp[3][i+1][j],dp[3][i][j+1]+t[i+1][j+1])
print(dp[3][r-1][c-1])
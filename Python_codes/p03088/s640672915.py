N = int(input())
mod = 10**9+7
dp = [[[[0 for i in range(4)] for j in range(4)] for k in range(4)] for l in range(N+2)]
banc = [(i,0,2) for i in range(4)] + [(0,2,i) for i in range(4)] + [(i,2,0) for i in range(4)] + [(0,i,2) for i in range(4)]
bang = [(i,0,1) for i in range(4)]
if N == 3:
    print(61)

else:

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (i,j,k) in ((0,2,1),(0,1,2),(2,0,1)):
                    continue
                dp[3][i][j][k] += 1
    
    for n in range(4,N+2):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if (i,j,k) in ((0,2,1),(0,1,2),(2,0,1)):
                            continue
                        if (l,i,j) in ((0,2,1),(0,1,2),(2,0,1)):
                            continue
                        if (l,i,j) in banc:
                            if k==1:
                                continue
                            dp[n][i][j][k] += dp[n-1][l][i][j]
                            dp[n][i][j][k] %= mod
                        elif (l,i,j) in bang:
                            if k==2:
                                continue
                            dp[n][i][j][k] += dp[n-1][l][i][j]
                            dp[n][i][j][k] %= mod
                        else:
                            dp[n][i][j][k] += dp[n-1][l][i][j]
                            dp[n][i][j][k] %= mod
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= mod
    print(ans)


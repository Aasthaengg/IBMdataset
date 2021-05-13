"""
21:12:30
"""
mod = 10**9 + 7
H, W, K = map(int, input().split())
# 残っている本数
bs = [1,2,3,5,8,13,21]

if W == 1:
    print(1)
    exit()
dp = [[0]*(W) for i in range(H+1)]
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        # 左端 : そのまま下ろす(j+1からｱﾐﾀﾞ)か、一つ右から下ろす(j+2からｱﾐﾀﾞ)
        if j == 0:
            dp[i+1][j] = dp[i][j] * bs[W-1-(j+1)] + dp[i][j+1] * bs[W-1-(j+2)]        
        # 右端 : そのまま下ろす(j-1からｱﾐﾀﾞ)か、一つ左から下ろす(j-2からｱﾐﾀﾞ)
        elif j == W-1:
            dp[i+1][j] = dp[i][j-1] * bs[j-2] + dp[i][j] * bs[j-1]   
        # 中    
        else:
            dp[i+1][j] = dp[i][j-1]*bs[max(0,j-2)]*bs[W-1-(j+1)] + dp[i][j]*bs[j-1]*bs[W-1-(j+1)] + dp[i][j+1]*bs[j-1]*bs[max(0,W-1-(j+2))]
        # print(dp[i+1])
        dp[i+1][j] %= mod
print(dp[H][K-1])
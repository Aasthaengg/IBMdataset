"""
dp[i][j] => i回目の移動が終了したタイミングでj列目にいる場合の数
dp[i][j] 
= dp[i-1][j-1]*(j-1列目とj列目の間に横棒があるような横棒の配置パターン数)
+ dp[i-1][j+1]*(j+1列目とj列目の間に横棒があるような横棒の配置パターン数)
+ dp[i-1][j]*(j列目の両サイドに横棒がないような横棒の配置パターン数)
"""

H,W,K = map(int,input().split())
mod = 10**9 +7

"""
横棒の配置パターンを前計算しておく
patternA[i] => i列目とi-1列目の間に横棒があるような横棒の配置パターン数
patternB[i] => i列目の両サイドに横棒がないような横棒の配置パターン数
"""
patternA = [0]*(W)
patternB = [0]*(W)
for i in range(2**(W-1)):
    pattern = format(i,"0"+str(W-1)+"b")
    for j in range(1,W-1):
        if pattern[j] == "1" and pattern[j-1]=="1":
            break
    else:
        for j in range(W-1):
            if pattern[j] == "1":
                patternA[j+1] += 1

        for j in range(W):
            if j == 0:
                if pattern[j] == "0":
                    patternB[j] += 1
            elif 0 < j < W-1:
                if pattern[j-1] == "0" and pattern[j] == "0":
                    patternB[j] += 1
            elif j == W-1:
                if pattern[j-1] == "0":
                    patternB[j] += 1

dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1

for i in range(1,H+1):
    for j in range(W):
        #左上から降りてくるパターン
        if j > 0:
            dp[i][j] += dp[i-1][j-1]*patternA[j]%mod
        #右上から降りてくるパターン
        if j < W-1:
            dp[i][j] += dp[i-1][j+1]*patternA[j+1]%mod
        
        #真上から降りてくるパターン
        dp[i][j] += dp[i-1][j]*patternB[j]%mod

        dp[i][j] %= mod

print(dp[-1][K-1])

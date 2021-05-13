"""
15,8,5の場合：
何回右に移動するか、何回左に移動するか。
dp[i][j] => i回目下降が終わった時点で、j列目にいる場合の数
memo[j] => 特定の高さを見たときに、j列目とj+1列目の間に横棒があるような横棒配置パターン数
memo2[j] => j列目の左右に横棒がないような場合の数
"""
mod = 10**9 +7
H,W,K = map(int,input().split())
if W == 1:
    print(1)
    exit()
memo = [0]*(W-1)
memo2 = [0]*(W-1)
cnt = 0
for i in range(2**(W-1)):
    binI = format(i,"0"+str(W-1)+"b")
    #パターンの有効性をチェックする
    for j in range(W-2):
        if binI[j] == "1" and binI[j+1] == "1":
            break
    else:
        cnt += 1
        for j in range(W-1):
            if binI[j] == "1":
                memo[j] += 1
        for j in range(1,W-1):
            if binI[j-1]=="0" and binI[j] =="0":
                memo2[j] += 1
dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        #右の列に移動する
        if j != W-1:
            dp[i+1][j+1] += memo[j]*dp[i][j]%mod
            dp[i+1][j+1] %= mod
        #左の列に移動する
        if j != 0:
            dp[i+1][j-1] += memo[j-1]*dp[i][j]%mod
            dp[i+1][j-1] %= mod
        #真下に移動する
        if j == 0:
            dp[i+1][j] += (cnt-memo[j])*dp[i][j]%mod
        elif j == W-1:
            dp[i+1][j] += (cnt-memo[j-1])*dp[i][j]%mod
        else:
            dp[i+1][j] += memo2[j]*dp[i][j]%mod
        dp[i+1][j]%=mod

print(dp[-1][K-1])
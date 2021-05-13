#0:09
"""
ABC数
遷移を考える問題
dp[どこまでみたか][その時の状態] = になりうる場合の数
"""
S = input()
n = len(S)

dp = [[0]*3 for i in range(n+1)]
cnt = 0 #はてなの数
#初期は後で構築
mod = 10**9 + 7 

X = 1
for i in range(n):
    if S[i] == "A":
        dp[i+1][0] = dp[i][0] + X
        dp[i+1][1] = dp[i][1]
        dp[i+1][2] = dp[i][2]
    elif S[i] == "B":
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = (dp[i][0] + dp[i][1]) % mod
        dp[i+1][2] = dp[i][2]
    elif S[i] == "C":
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
        dp[i+1][2] = (dp[i][1] + dp[i][2]) % mod
    elif S[i] == "?":
        dp[i+1][0] = (dp[i][0] * 3 + X) % mod
        dp[i+1][1] = (dp[i][1] * 3)%mod + (dp[i][0]) % mod
        dp[i+1][2] = (dp[i][2] * 3)%mod + (dp[i][1]) % mod        
        X = (X*3)%mod
print(dp[n][2]%mod)
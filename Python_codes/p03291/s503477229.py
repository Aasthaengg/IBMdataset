S = input()
#dp[i][four] =: i + 1番目まで見たとき,照合したケツがfourとなるものの総数
dp = [[0 for _ in range(4)] for _ in range(len(S)+1 )]
dp[0][0] = 1
mod = 10**9 + 7
for i in range(len(S)):
    if S[i] == '?':
        dp[i+1][1] += dp[i][0] 
        dp[i+1][1] %= mod
        dp[i+1][2] += dp[i][1] 
        dp[i+1][2] %= mod
        dp[i+1][3] += dp[i][2] 
        dp[i+1][3] %= mod
    if S[i] == 'A':
        dp[i+1][1] += dp[i][0] 
        dp[i+1][1] %= mod
    if S[i] == 'B':
        dp[i+1][2] += dp[i][1]
        dp[i+1][2] %= mod
    if S[i] == 'C':
        dp[i+1][3] += dp[i][2]
        dp[i+1][3] %= mod
    for f in range(4):
        if S[i] != '?':
            dp[i+1][f] += dp[i][f]
        else:
            dp[i+1][f] += dp[i][f] * 3
        dp[i+1][f] %= mod
print(dp[len(S)][3]%mod)

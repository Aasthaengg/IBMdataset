MOD = 1000000007

S = input()
N = len(S)

dp = [[0, 0, 0, 0] for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    if S[i] == '?':
        for j in range(4):
            dp[i + 1][j] += dp[i][j] * 3
            dp[i + 1][j] %= MOD
    else:
        for j in range(4):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            
    if S[i] == 'A' or S[i] == '?':
        dp[i + 1][1] += dp[i][0]
        dp[i + 1][1] %= MOD
        
    if S[i] == 'B' or S[i] == '?':
        dp[i + 1][2] += dp[i][1]
        dp[i + 1][2] %= MOD
        
    if S[i] == 'C' or S[i] == '?':
        dp[i + 1][3] += dp[i][2]
        dp[i + 1][3] %= MOD

print(dp[N][3])
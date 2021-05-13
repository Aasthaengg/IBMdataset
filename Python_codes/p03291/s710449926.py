S = input()
dp = [[0 for i in range(4)] for i in range(len(S)+1)]
MOD = 10**9+7
dp[0][3] = 1
for i in range(len(S)):
    if S[i] == '?': k = 3
    else: k = 1
    for _ in range(k):
        dp[i+1][0] += dp[i][0] 
        dp[i+1][1] += dp[i][1] 
        dp[i+1][2] += dp[i][2] 
        dp[i+1][3] += dp[i][3] 
    if S[i] == 'A':
        dp[i+1][0] +=  dp[i][3]
    elif S[i] == 'B':
        dp[i+1][1] +=  dp[i][0]
    elif S[i] == 'C':
        dp[i+1][2] += dp[i][1]
    else:
        dp[i+1][0] += dp[i][3]
        dp[i+1][1] += dp[i][0]
        dp[i+1][2] += dp[i][1]
    for j in range(4):
        if dp[1+i][j] > MOD: dp[i+1][j] %= MOD
print(dp[len(S)][2]%MOD)

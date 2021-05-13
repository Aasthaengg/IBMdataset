S = input()
N = len(S)
MOD = 10**9 + 7
mask = 'ABC'

dp = [[0,0,0,0] for _ in range(N+1)]

for i in range(N, -1, -1) :
    for j in range(4) :
        if i == N :
            if j == 3 :
                dp[i][j] = 1
            else :
                dp[i][j] = 0
        else :
            if j == 3 :
                weight = 3 if S[i] == '?' else 1
                dp[i][j] = weight * dp[i+1][j]
            else :
                weight = 3 if S[i] == '?' else 1
                able = 1 if (S[i] == mask[j] or S[i] == '?') else 0
                dp[i][j] = weight * dp[i+1][j] + able * dp[i+1][j+1]
            dp[i][j] %= MOD


print(dp[0][0] % MOD)
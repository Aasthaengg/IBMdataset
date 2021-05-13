S = input()
N = len(S)
m = 10**9 + 7

dp = [[0]*(N+1) for _ in range(13)]
dp[0][0] = 1

for i in range(N):
    p = pow(10,i,13)
    for j in range(13):
        digit = S[N-1-i]
        if digit == '?':
            for k in range(10):
                d = (j+k*p%13)%13
                dp[d][i+1] += dp[j][i]
                dp[d][i+1] %= m

        else:
            k = int(digit)
            d = (j+k*p%13)%13
            dp[d][i+1] += dp[j][i]
            dp[d][i+1] %= m
print(dp[5][N])

L = input()
N = len(L)
MOD = 10**9 + 7

dp = [[0 for _ in range(2)] for _ in range(N+1)]
dp[0][0] = 1


for i in range(N):
    if L[i] == "1":
        dp[i+1][1] += dp[i][1] * 3 # (a,b) = (0,0),(1,0),(0,1)
        dp[i+1][1] += dp[i][0] # (0,0)
        dp[i+1][0] += dp[i][0] * 2 # (1,0) (0,1)
    else:
        dp[i+1][1] += dp[i][1] * 3 # (a,b) = (0,0),(1,0),(0,1)
        # dp[i+1][1] += dp[i][0] # a + b = a xor b を満たせないので、この遷移はない
        dp[i+1][0] += dp[i][0]  # (0,0) 

    dp[i+1][1] %= MOD
    dp[i+1][0] %= MOD
    

print(sum(dp[-1]) % MOD)
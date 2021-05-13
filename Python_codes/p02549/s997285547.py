MOD = 998244353
N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]

dp = [0]*(N+1)
acc = [0]*(N+1) # acc[i] = dp[1] + ... dp[i]

dp[1] = 1
acc[1] = 1
for i in range(2, N+1):
    for lr in LR:
        l = lr[0]
        r = lr[1]

        dp[i] += (acc[max(0, i - l)] - acc[max(0, i - r - 1)] + MOD)
        dp[i] %= MOD
    acc[i] = (acc[i-1] + dp[i]) % MOD
    
    

print(dp[N])
# print(acc)
# print(dp[N])
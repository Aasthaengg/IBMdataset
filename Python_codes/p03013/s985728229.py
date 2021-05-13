n, m = list(map(int, input().split()))

MOD = pow(10, 9) + 7

dp = [0] * (n+1)

dp[0] = 1

broken = [False] * (n+1)
for i in range(m):
    broken[int(input())] = True

c = 1

for i in range(1, n+1):
    if broken[i]:
        dp[i] = 0
    else:
        if i == 1:
            dp[i] = dp[i-1] % MOD
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[-1] % MOD) 

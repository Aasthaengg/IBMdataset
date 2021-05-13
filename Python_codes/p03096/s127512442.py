N = int(input())
C = [int(input()) for _ in range(N)]
MOD = 10**9 + 7
subC = [-2] * (2 * 10 ** 5 + 10)
cntC = [-1]*N
for num, i in enumerate(C):
    cntC[num] = subC[i]+1
    subC[i] = num

# print(cntC)

dp = [0] * (N + 10)
dp[0] = 1
for i in range(N):
    if cntC[i] < 0 or cntC[i] == i:
        dp[i + 1] = dp[i] % MOD
    else:
        dp[i + 1] = (dp[i] + dp[cntC[i]]) % MOD


print(dp[N])
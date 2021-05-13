A = [1,6,9,36,81,216,729,1296,6561,7776,46656,59049]
N = int(input())

dp = [N] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    for j in A:
        if i >= j:
            dp[i] = min(dp[i], dp[i - j] + 1)

print(dp[N])
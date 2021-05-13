N = int(input())
P = list(map(float, input().split()))

dp = [0 for _ in range(N + 1)]
dp[0] = 1

for i in range(N):
    p = P[i]
    for j in range(N)[::-1]:
        dp[j + 1] += dp[j] * p
        dp[j] *= 1 - p

print(sum(dp[N // 2 + 1:]))
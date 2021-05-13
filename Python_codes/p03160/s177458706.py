N = int(input())
jumps = [int(n) for n in input().split()]

dp = [float("inf")] * N
dp[0] = 0

for i in range(N - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(jumps[i] - jumps[i + 1]))
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(jumps[i] - jumps[i + 2]))

print(dp[-1])
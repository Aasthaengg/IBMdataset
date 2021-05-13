N = int(input())
steps = list(map(int, input().split()))

dp = [99999999] * N
dp[0] = 0
for i in range(1, N):
    a = abs(steps[i] - steps[i - 1]) + dp[i - 1]
    if i < 2:
        dp[i] = a
        continue
    b = abs(steps[i] - steps[i - 2]) + dp[i - 2]
    dp[i] = a if a <= b else b

print(dp[N - 1])

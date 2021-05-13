N = int(input())
P = [float(i) for i in input().split()]

dp = [0.0] * (N + 1)
dp[0] = 1.0

for i, p in enumerate(P, 1):
    dp = [p * a + (1 - p) * b for a, b in zip([0] + dp, dp)]

print(sum(dp[-(-N // 2):]))
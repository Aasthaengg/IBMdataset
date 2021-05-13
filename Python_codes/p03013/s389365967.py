N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]


dp = [0] * (N + 1)
dp[0] = 1

# 行けない段
for ai in a:
    dp[ai] = -1

for i in range(1, N + 1):
    # 1段目だけ例外処理
    if i == 1:
        dp[1] += dp[0]

    elif i > 1 and dp[i] != -1:
        if dp[i - 2] != -1:
            dp[i] += dp[i - 2]
        if dp[i - 1] != -1:
            dp[i] += dp[i - 1]

print(dp[N] % (10**9 + 7))

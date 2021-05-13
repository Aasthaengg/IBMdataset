n, k = map(int, input().split())
a = list(map(int, input().split()))

MAX_DIGIT = 40

dp = [[-1, -1] for _ in range(MAX_DIGIT+1)]
dp[0][0] = 0
for i in range(MAX_DIGIT):
    mask = 1 << (MAX_DIGIT - i - 1)
    cnt_1 = 0
    for v in a:
        if v & mask:
            cnt_1 += 1
    cnt_0 = n - cnt_1

    cost_0 = mask * cnt_1
    cost_1 = mask * cnt_0

    if dp[i][1] != -1:
        dp[i+1][1] = max(dp[i+1][1], dp[i][1] + max(cost_0, cost_1))

    if k & mask:
        dp[i+1][1] = max(dp[i+1][1], dp[i][0] + cost_0)

    if k & mask:
        dp[i+1][0] = max(dp[i+1][0], dp[i][0] + cost_1)
    else:
        dp[i+1][0] = max(dp[i+1][0], dp[i][0] + cost_0)

print(max(dp[MAX_DIGIT][0], dp[MAX_DIGIT][1]))
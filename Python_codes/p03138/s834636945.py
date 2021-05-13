N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(41)]
dp[40][0] = 0

for d in range(1, 41):
    if dp[d-1][1] == 1:
        dp[d][1] = 1

    mask = 1 << (40 - d)
    num_1 = 0
    for i in range(N):
        if A[i] & mask:
            num_1 += 1

    if num_1 >= N - num_1:      # i行目は0にする
        dp[d][0] = dp[d-1][0] + num_1 * (2 ** (40-d))
        if K & mask:
            dp[d][1] = 1
    else:                       # i行目は1にする
        if dp[d][1]:
            dp[d][0] = dp[d-1][0] + (N - num_1) * (2 ** (40 - d))
        else:
            if K & mask:
                dp[d][0] = dp[d-1][0] + (N - num_1) * (2 ** (40 - d))
            else:
                dp[d][0] = dp[d-1][0] + num_1 * (2 ** (40 - d))

print(dp[-1][0])
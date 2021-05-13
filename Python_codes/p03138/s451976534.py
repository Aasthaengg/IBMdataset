
# 桁DP
N, K = map(int,input().split())
A = list(map(int,input().split()))
dp = [[-1]*2 for _ in range(100)]
MAX_DIGIT = 50

dp[0][0] = 0
for i in range(MAX_DIGIT):
    bitmask = 1 << (MAX_DIGIT-i-1)
    bit1_num = 0
    for a in A:
        if bitmask & a:
            bit1_num += 1

    score0 = bitmask*bit1_num  # Xのi桁目を0した時のfへの寄与
    score1 = bitmask*(N-bit1_num)

    if dp[i][1] != -1:
        dp[i+1][1] = max(dp[i+1][1],dp[i][1] + max(score0,score1))

    if dp[i][0] != -1:
        if K & bitmask:
            dp[i+1][1] = max(dp[i+1][1],dp[i][0] + score0)

    if dp[i][0] != -1:
        if K & bitmask:
            dp[i+1][0] = max(dp[i+1][0],dp[i][0] + score1)
        else:
            dp[i+1][0] = max(dp[i+1][0], dp[i][0] + score0)


ans = max(dp[MAX_DIGIT][0], dp[MAX_DIGIT][1])
print(ans)
R, C, K = map(int, input().split())
inf = float('inf')
v_list = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    v_list[r - 1][c - 1] = v

dp = [[0, 0, 0, 0] for _ in range(C)]
for r in range(R):
    for c in range(C):
        if c > 0:
            dp[c][0] = max(dp[c])
            dp[c][1] = dp[c - 1][1]
            dp[c][2] = dp[c - 1][2]
            dp[c][3] = dp[c - 1][3]
        else:
            dp[c][0] = max(dp[c])
            dp[c][1] = 0
            dp[c][2] = 0
            dp[c][3] = 0
        if v_list[r][c] > 0:
            v = v_list[r][c]
            dp[c][3] = max(dp[c][2] + v, dp[c][3])
            dp[c][2] = max(dp[c][1] + v, dp[c][2])
            dp[c][1] = max(dp[c][0] + v, dp[c][1])            
print(max(dp[-1]))
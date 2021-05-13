n, k = map(int, input().split())
heights = [int(x) for x in input().split()]

dp = [[float("inf") for _ in range(k + 1)] for _ in range(n)]
for i in range(0, k + 1):
    dp[0][i] = 0
for i in range(n):
    for j in range(1, k + 1):
        if i + j < n:
            # dp[i + j][j] = min(dp[i + j][j], dp[i][j] + abs(heights[i] - heights[i + j]))
            val1 = dp[i + j][j]
            val2 = dp[i][0] + abs(heights[i] - heights[i + j])
            if val2 < val1:
                dp[i + j][j] = val2
                if dp[i + j][0] > val2:
                    dp[i + j][0] = val2
        # if i == 0 and j == 1:
        #     print("here")
        #     print(dp[i][j], abs(heights[i] - heights[i + j]))
# result = float("inf")
# for i in range(1, k + 1):
#     result = min(result, dp[-1][i])
# print(result)
# print(dp)
print(dp[-1][0])
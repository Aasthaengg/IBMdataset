n = int(input())
candy_map = []
candy_map.append(list(map(int, input().split())))
candy_map.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(2)]
dp[0][0] = candy_map[0][0]
for i in range(1,n):
    dp[0][i] = dp[0][i-1] + candy_map[0][i]
dp[1][0] = dp[0][0] + candy_map[1][0]
for i in range(1,n):
    dp[1][i] = candy_map[1][i] + max(dp[0][i],dp[1][i-1])
print(dp[1][-1])

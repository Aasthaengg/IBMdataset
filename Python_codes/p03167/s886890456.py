H, W = map(int, input().split())
A = [input() for _ in range(H)]
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
MOD = 10**9 + 7
for y in range(0, H):
    for x in range(0, W):
        if A[y][x] == '#':
            continue

        if x - 1 >= 0:
            dp[y][x] += dp[y][x-1]
            dp[y][x] %= MOD
        if y - 1 >= 0:
            dp[y][x] += dp[y-1][x]
            dp[y][x] %= MOD
# print(*dp, sep='\n')
print(dp[-1][-1])

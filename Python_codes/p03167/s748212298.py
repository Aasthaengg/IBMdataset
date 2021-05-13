h, w = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(h)]
MOD = 10**9 + 7

# dpテーブル
dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[1][1] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if arr[i - 1][j - 1] == "#":
            continue
        else:
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

print(dp[h][w] % MOD)
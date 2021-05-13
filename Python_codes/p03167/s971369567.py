h, w = [int(i) for i in input().split()]
mod = 10 ** 9 + 7
dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][0] = 1
for i in range(h):
    a = input()
    for j, k in enumerate(a):
        if i == 0 and j == 0:
            continue
        if k != "#":
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod
print(dp[h-1][w-1])

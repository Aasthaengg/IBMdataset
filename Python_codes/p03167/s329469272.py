H,W = map(int,input().split())
A = [list(input()) for _ in range(H)]
mod = 10 ** 9 + 7

dp = [[0] * (W + 1) for _ in range(H + 1)]
dp[1][1] = 1

for x in range(1,W+1):
    for y in range(1,H+1):
        if x == y == 1:
            continue
        else:
            if A[y-1][x-1] != '#' and (dp[y-1][x] > 0 or dp[y][x-1] > 0):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
print(dp[H][W] % mod)
H, W, K = map(int, input().split())

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
mod = 10 ** 9 + 7
'''
端にいてそのまま下にいくときfib[W+1]
端にいて右か左にいくときfib[W]
中にいて下に行くとき
'''
if W == 1:
    print(1)
    exit()

dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1
for h in range(1, H + 1):
    for w in range(W):
        if w == 0:
            # 上からくるか右からくるかのどちらか
            dp[h][w] = dp[h - 1][w] * fib[W - 1] + dp[h - 1][w + 1] * fib[W - 2]
        elif w == W - 1:
            dp[h][w] = dp[h - 1][w] * fib[W - 1] + dp[h - 1][w - 1] * fib[W - 2]
        else:
            dp[h][w] = dp[h - 1][w] * fib[w] * fib[W - 1 - w] + dp[h - 1][w + 1] * fib[W - w - 2] * fib[w] + dp[h - 1][
                w - 1] * fib[
                           w - 1] * fib[W - 1 - w]
        dp[h][w] %= mod

print(dp[H][K - 1])

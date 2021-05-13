import itertools

MOD = 10 ** 9 + 7

H, W = map(int, input().split())
A = [input() for _ in range(H)]

dp = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
dp[1][1] = 1

it = itertools.product(range(H), range(W))
next(it)
for h, w in it:
    if A[h][w] == '.':
        dp[h + 1][w + 1] = (dp[h][w + 1] + dp[h + 1][w]) % MOD
print(dp[H][W])

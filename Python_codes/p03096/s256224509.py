from collections import defaultdict

MOD = 10 ** 9 + 7

N = int(input())
c = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N + 1)]
dp[0] = 1

d = defaultdict(lambda: -1)

for i, cc in enumerate(c, 1):
    if c[i - 1] == c[i - 2]:
        dp[i] = dp[i - 1]
    elif d[cc] == -1:
        # 初めて出現した色
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[d[cc]]
    dp[i] %= MOD
    d[cc] = i
    # print(d)
    # print(dp)
print(dp[N])
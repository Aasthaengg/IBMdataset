
def chmin(a, b): return b if a > b else a


def chmax(a, b): return a if a > b else b


"""もらうDP"""
import math

N = int(input())
h = list(map(int, input().split()))

dp = list([math.inf for i in range(N)])  # dpテーブル
dp[0] = 0
for i in range(N):
    dp[i] = chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    if i > 1:
        dp[i] = chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

print(dp[N-1])

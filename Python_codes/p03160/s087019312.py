import sys
input = sys.stdin.readline

INF = 10 ** 60

def li():
    return [int(x) for x in input().split()]


N = int(input())
h = li()

dp = [INF] * N

# 初期条件
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    dp[i] = min(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]))
    dp[i] = min(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]))

print(dp[N - 1])
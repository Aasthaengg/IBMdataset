import sys

input = sys.stdin.readline
mod = 10 ** 9 + 7
n, m = map(int, input().split())
dp = [0] * (n + 1)
dp[0] = 1
ng = set(int(input()) for _ in range(m))

for i in range(n):
    next1 = i + 1
    if next1 not in ng:
        dp[next1] += dp[i]
        dp[next1] %= mod
    next2 = i + 2
    if next2 not in ng and next2 <= n:
        dp[next2] += dp[i]
        dp[next2] %= mod
print(dp[-1])
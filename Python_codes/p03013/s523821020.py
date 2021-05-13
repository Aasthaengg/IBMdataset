import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7

n, m = map(int, readline().split())
a = list(map(int, read().split()))

dp = [0] * (n + 1)
ng = [0] * (n + 1)

for i in a:
    ng[i] = 1

dp[0] = 1
if ng[1] != 1:
    dp[1] = 1

for i in range(2, n + 1):
    if ng[i - 1] == 1 and ng[i - 2] == 1:
        print(0)
        exit()
    elif ng[i - 1] == 1:
        dp[i] = dp[i - 2]
    elif ng[i - 2] == 1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
    if dp[i] > MOD:
        dp[i] %= MOD

print(dp[-1])
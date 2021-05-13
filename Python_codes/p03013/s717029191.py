import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7

n, m = map(int, readline().split())
a = list(map(int, read().split()))

dp = [0] * (n + 1)
ok = [1] * (n + 1)

for i in a:
    ok[i] = 0

dp[0] = 1
dp[1] = 1 * ok[1]

for i in range(2, n + 1):
    if ok[i - 1] == 0 and ok[i - 2] == 0:
        print(0)
        exit()
    else:
        dp[i] = dp[i - 1]*ok[i - 1] + dp[i - 2]*ok[i - 2]
    if dp[i] > MOD:
        dp[i] %= MOD

print(dp[-1])
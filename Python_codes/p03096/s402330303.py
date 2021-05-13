from bisect import bisect_left
MOD = 10 ** 9 + 7

n = int(input())
clst = []
last = [-1 for _ in range(2 * 10 ** 5)]
before = [-1 for _ in range(2 * 10 ** 5)]
for i in range(n):
    c = int(input())
    clst.append(c - 1)
    before[i] = last[c - 1]
    last[c - 1] = i
dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    dp[i] = dp[i - 1]
    if before[i] != -1 and before[i] != i - 1:
        pos = before[i]
        dp[i] += dp[pos]
    dp[i] %= MOD
print(dp[-1])
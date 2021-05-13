mod = 10 ** 9 + 7
n = int(input())
c = [int(input()) for _ in range(n)]
import copy
cc = copy.deepcopy(c)
color_sum = {i: 0 for i in range(10 ** 6)}
dp = [1 for _ in range(n + 1)]
color_sum[cc[0]] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1]
    if cc[i - 2] == cc[i - 1]:
        continue
    dp[i] += color_sum[cc[i - 1]]
    dp[i] %= mod
    color_sum[c[i - 1]] += dp[i - 1]
    color_sum[c[i - 1]] %= mod
print(dp[n])
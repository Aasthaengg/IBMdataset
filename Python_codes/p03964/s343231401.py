n = int(input())
ta = [list(map(int, input().split())) for _ in range(n)]

import math
dp = ta[0]
for i in range(1, n):
    t = ta[i][0]
    a = ta[i][1]

    k1 = dp[0] // t
    if k1 * t != dp[0]:
        k1 += 1
    k2 = dp[1] // a
    if k2 * a != dp[1]:
        k2 += 1
    k = max(k1, k2)

    dp = [k * t, k * a]
print(sum(dp))


import math
from pprint import pprint


def submit():
    n = int(input())
    p = list(map(float, input().split()))

    dp = [[0 for _ in range(i + 1)] for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(i + 1):
            dp[i + 1][j] += (1 - p[i]) * dp[i][j]
            dp[i + 1][j + 1] += p[i] * dp[i][j]

    thr = n // 2
    ans = 0
    for i in range(thr + 1, n + 1):
        ans += dp[n][i]

    print(ans)

submit()
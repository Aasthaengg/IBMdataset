from __future__ import division
from sys import stdin, maxint

def solve(n, m, ds):
    dp = [maxint] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(m):
            if i >= ds[j]:
                dp[i] = min(dp[i], dp[i - ds[j]] + 1)

    return dp[n]

if __name__ == '__main__':
    n, m = map(int, stdin.readline().strip().split())
    ds = map(int, stdin.readline().strip().split())
    print(solve(n, m, ds))
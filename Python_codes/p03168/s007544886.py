import sys
import numpy as np

sys.setrecursionlimit(10 ** 9)
#def input():
#    return sys.stdin.readline()[:-1]

N = int(input())
P = list(map(float,input().split()))

dp = np.zeros(N+1, dtype=float)
dp[0] = 1

for c in P:
#    prev = dp.copy()
    dp = np.append(dp[:-1] * (1-c), 0) + np.append(0, dp[:-1] * c)
#    print(dp)

ans = np.sum(dp[N//2+1:])
print(ans)

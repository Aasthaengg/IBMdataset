import sys
import math
import fractions
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**7)

H, W, K = map(int, input().split())

if W == 1:
    print(1)
    exit(0)


pattern = [0] * (W - 1)
total = 0
for i in range(2 ** (W - 1)):
    bit = format(i, 'b').zfill(W - 1)
    flag = True
    for j in range(W - 1):
        if j >= 1 and bit[j] == bit[j - 1] == "1":
            flag = False
    if flag:
        total += 1
        for j in range(W - 1):
            if bit[j] == "1":
                pattern[j] += 1

dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1

for i in range(1, H + 1):
    for j in range(W):
        if j == 0:
            dp[i][j] += dp[i - 1][j + 1] * pattern[j]
            dp[i][j] %= 1000000007
            dp[i][j] += dp[i - 1][j] * (total - pattern[j])
            dp[i][j] %= 1000000007
        elif j == W - 1:
            dp[i][j] += dp[i - 1][j - 1] * pattern[j - 1]
            dp[i][j] %= 1000000007
            dp[i][j] += dp[i - 1][j] * (total - pattern[j - 1])
            dp[i][j] %= 1000000007
        else:
            dp[i][j] += dp[i - 1][j + 1] * pattern[j]
            dp[i][j] %= 1000000007
            dp[i][j] += dp[i - 1][j - 1] * pattern[j - 1]
            dp[i][j] %= 1000000007
            dp[i][j] += dp[i - 1][j] * (total - pattern[j - 1] - pattern[j])
            dp[i][j] %= 1000000007

print(dp[H][K - 1])

#!/usr/bin/env python
# DP解

x = int(input())
dp = [False for _ in range(x+1)]
dp[0] = True

if 1 <= x < 100:
    print(0)
    exit()

for i in range(1, 100):
    dp[i] = False
for i in range(100, x+1):
    tmp = False
    for j in range(6):
        if i-(100+j) >= 0:
            tmp = (tmp or dp[i-(100+j)])
    if tmp:
        dp[i] = True
    else:
        dp[i] = False

if dp[x]:
    print(1)
else:
    print(0)

# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 24/07/2020

from sys import stdin,stdout
from math import gcd, ceil, sqrt
from collections import Counter
from bisect import bisect_left, bisect_right
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
mod = 1000000007

n, k = iia()
arr = iia()
dp = [0] * n
for i in range(1, n):
    cur = float("inf")
    for j in range(1, k + 1):
        if i - j >= 0:  
            t = abs(arr[i] - arr[i - j]) + dp[i - j]
            cur = min(cur, t)
        else:
            break
    dp[i] = cur
print(dp[-1])

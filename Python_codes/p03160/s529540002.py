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

n = ii1()
arr = iia()
dp = [0] * n
dp[1] = abs(arr[1] - arr[0])
for i in range(2, n):
    t1 = abs(arr[i] - arr[i - 2]) + dp[i - 2]
    t2 = abs(arr[i] - arr[i - 1]) + dp[i - 1]
    dp[i] = min(t1, t2)
print(dp[-1])

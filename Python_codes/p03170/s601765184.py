# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 01/08/2020

from sys import stdin, stdout, setrecursionlimit
from math import gcd, ceil, sqrt
from collections import Counter
from bisect import bisect_left, bisect_right
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
setrecursionlimit(100000)
mod = 1000000007

n, k = iia()
arr = iia()
dp = [False for i in range(k + 1)]
for i in range(k + 1):
    for j in arr:
        if i >= j and not dp[i - j]:
            dp[i] = True
if dp[-1]:
    print('First')
else:
    print('Second')
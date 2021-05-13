# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 31/07/2020

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

h, w = iia()
arr = []
for i in range(h):
    arr.append(list(is1()))
dp = [[0 for i in range(w)] for j in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if i > 0 and j > 0 and arr[i][j] == '.':
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        elif i > 0 and arr[i][j] == '.':
            dp[i][j] = dp[i - 1][j]
        elif j > 0 and arr[i][j] == '.':
            dp[i][j] = dp[i][j - 1]
print(dp[-1][-1] % mod)
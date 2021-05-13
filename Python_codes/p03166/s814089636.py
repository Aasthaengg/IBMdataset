# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 01/08/2020

from sys import stdin, stdout
import sys
from math import gcd, ceil, sqrt
from collections import Counter
from bisect import bisect_left, bisect_right
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
mod = 1000000007
sys.setrecursionlimit(100000)
n, m = iia()
dp = [-1] * (n + 1)
d = {}
for i in range(m):
    a, b = iia()
    d.setdefault(a, []).append(b)

def dfs(cur):
    if dp[cur] != -1:
        return dp[cur]
    t = 0
    for i in d.get(cur, []):
        t = max(1 + dfs(i), t)
    dp[cur] = t
    return dp[cur]

res = 0
for i in range(1, n + 1):
    res = max(res, dfs(i))
print(res)
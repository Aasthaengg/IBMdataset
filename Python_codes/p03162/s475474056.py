# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 30/07/2020

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
cur = None
for i in range(n):
    a, b, c = iia()
    if not cur:
        cur = [a, b, c]
    else:
        t1 = max(cur[1], cur[2]) + a
        t2 = max(cur[0], cur[2]) + b
        t3 = max(cur[0], cur[1]) + c
        cur = [t1, t2, t3]
print(max(cur))
import sys
sys.setrecursionlimit(1000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from math import *

N = int(input())
s, t = input(), input()
mod = 10**9+7
ans = 1
pre = -1
for a, b in zip(s, t):
    if pre == 0:
        ans *= 2
        if a == b:
            pre = 0
        else:
            pre = 1
    elif pre == 1:
        pre = 2
    elif pre == 2:
        if a == b:
            pre = 0
        else:
            ans *= 3
            pre = 1
    else:
        if a == b:
            ans *= 3
            pre = 0
        else:
            ans *= 6
            pre = 1
    ans %= mod
print(ans)


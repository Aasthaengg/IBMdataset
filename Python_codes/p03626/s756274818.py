import bisect
import collections
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7

N = int(input())
S1 = list(input())
S2 = list(input())
a = []
now = 0
while now < N:
    if S1[now] == S2[now]:
        a.append("s")
        now += 1
    else:
        a.append("d")
        now += 2

for i in range(len(a)):
    if i == 0:
        if a[i] == "s":
            ans = 3
        else:
            ans = 6
    else:
        if a[i-1] == "s":
            ans *= 2
        else:
            if a[i] == "d":
                ans *= 3

print(ans%MOD)
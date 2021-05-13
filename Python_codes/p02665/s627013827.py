import sys
import math
import itertools
import collections
import heapq
import numpy as np

rl = sys.stdin.readline

n = int(rl())

li = list(map(int, rl().split()))
if n == 0 and li[0] == 1:
    print(1)
    exit()

can = [1-li[0]]

a = can[0]
for i in range(1, n+1):
    a = a*2
    can.append(a)
    a -= li[i]
    if a < 0:
        print(-1)
        exit()

ans = 0
can.reverse()
li.reverse()
temp = 0
for i in range(n+1):
    temp += li[i]
    ans += min(can[i], temp)
print(ans)
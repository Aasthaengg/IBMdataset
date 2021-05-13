from collections import defaultdict as dd
from collections import deque
import bisect
import heapq
import math

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    r = ri()
    print (2 * r * math.pi)






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()

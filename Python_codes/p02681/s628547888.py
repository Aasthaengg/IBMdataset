from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    s = input()
    t = input()
    if len(s) == len(t) - 1 and s == t[:-1]:
        print ("Yes")
    else:
        print ("No")





mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()

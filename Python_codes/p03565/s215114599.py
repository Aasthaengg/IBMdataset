# -*- coding: utf-8 -*-
import re
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

sys.setrecursionlimit(10**6)


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


def is_match(a, b):
    for _a, _b in zip(a, b):
        if (_a == _b or _a == '?'):
            continue
        else:
            return False
    return True


s = S()
t = S()

# s = s.replace('?', '.')
# pattern =   ''

if (t in s):
    print(s.replace('?', 'a'))
    exit()
if (len(s) < len(t)):
    print('UNRESTORABLE')
    exit()


if (is_match(s[-len(t):], t)):
    ans = s[:-len(t)] + t
    ans = ans.replace('?', 'a')
    print(ans)
    exit()
i = 0

for _s in reversed(s[len(t)-1:-1]):
    i += 1
    if (_s == t[-1] or _s == '?'):
        if (is_match(s[-i - len(t): - i], t)):
            ans = s[:-i - len(t)] + t + s[-i:]
            ans = ans.replace('?', 'a')
            print(ans)
            exit()


print('UNRESTORABLE')

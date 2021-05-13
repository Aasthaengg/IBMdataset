#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf
# @pysnooper.snoop()
#import pysnooper # debug

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect



class ModInt(int):

    MOD = None

    def __add__(self, other):
        self = ModInt(int.__add__(self, other) % ModInt.MOD)
        return self

    def __mul__(self, other):
        self = ModInt(int.__mul__(self, other) % ModInt.MOD)
        return self

def make_2d_arr(s1, s2, default=0):
    a = [None] * s1
    for i, _ in enumerate(a):
        a[i] = [default] * s2
    return a


if __name__ == '__main__':
    n, s = list(map(int, input().split()))
    data = list(map(int, input().split()))

    ModInt.MOD = 998244353
    dp = [ModInt(0)] * (s + 1)
    dp[0] = 1
    dp_arr = [dp, dp[:]]
    frm = 0
    to = 1

    for i in range(n):
        frm, to = to, frm
        for v in range(s + 1):
            dp_arr[to][v] = dp_arr[frm][v] * 2
            src = v - data[i]
            if src >= 0:
                dp_arr[to][v] += dp_arr[frm][src]
    #print('dp_arr') # debug
    #pp(dp_arr) # debug
    print(dp_arr[to][s])




    #print('\33[32m' + 'end' + '\033[0m') # debug

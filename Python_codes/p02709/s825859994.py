#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pp
from pprint import pformat as pf

import math
#from sortedcontainers import SortedList, SortedDict, SortedSet # no in atcoder
import bisect


class Solver:

    def __init__(self, n, students):
        self.n = n
        self.students = students
        self.ordered = self.make_ordered() # var[i] = (active, pos), dec ordered
        self.dp = self.make_dp_container() # var[l][r] = max ans

    def make_ordered(self):
        ordered = [None] * self.n
        for i, active in enumerate(self.students):
            pos = i
            #pos = i + 1
            ordered[i] = (active, pos)
        ordered = sorted(ordered, key=lambda tpl: tpl[0])
        ordered = list(reversed(ordered))
        return ordered

    def make_dp_container(self):
        dp = [None] * (self.n + 1)
        for i, _ in enumerate(dp):
            dp[i] = [0] * (self.n + 1)
        return dp

    def run(self):
        for s, (active, pos) in enumerate(self.ordered):
            for l in range(s + 1):
                v = active * abs(pos - l)
                self.update(s + 1, l + 1, self.dp[s][l] + v)
                r = s - l
                r_key = self.n - 1 - r
                v = active * abs(pos - r_key)
                self.update(s + 1, l, self.dp[s][l] + v)
        #print('self.dp') # debug
        #print(self.dp) # debug
        ans = max(self.dp[-1])
        return ans

    def update(self, s, l, value):
        self.dp[s][l] = max(self.dp[s][l], value)


if __name__ == '__main__':
    n = int(input())
    students = list(map(int, input().split()))
    ans = Solver(n, students).run()
    #print('ans') # debug
    print(ans)

    #print('\33[32m' + 'end' + '\033[0m') # debug

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

class Solver:

    def __init__(self, n, k):
        self.n = n
        self.k = k
        #fprint('k') # debug
        #fprint(k) # debug
        self.ans_list = [0] * (k + 1) # var[i] = count of gcd() == i case
        #fprint('self.ans_list') # debug
        #fprint(self.ans_list) # debug
        self.m = 10 ** 9 + 7

    def gcd_count(self, i):
        times = k // i
        cases = pow(times, n, self.m)
        j = i * 2
        while not (j > k):
            cases -= self.ans_list[j]
            j += i
        #fprint('i') # debug
        #fprint(i) # debug
        self.ans_list[i] = cases % self.m

    def run(self):
        for i in range(k, 0, -1):
            #print('i') # debug
            #print(i) # debug
            self.gcd_count(i)
        ans = 0
        for i, a in enumerate(self.ans_list):
            ans += i * a
        #fprint('self.ans_list') # debug
        #fprint(self.ans_list) # debug
        return ans % self.m



if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    ans = Solver(n, k).run()
    #fprint('ans') # debug
    print(ans)


    #fprint('\33[32m' + 'end' + '\033[0m') # debug

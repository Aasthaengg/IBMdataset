from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353

L, R = map(int, input().split())

if R-L >=2018:
    print(0)
else:
    ans = ((L%2019)*(R%2019))%2019
    for i in range(L,R+1):
        for j in range(i+1,R+1):
            ans = min(ans, ((i%2019)*(j%2019))%2019)
    print(ans)

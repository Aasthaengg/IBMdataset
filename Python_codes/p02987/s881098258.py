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

S = input()

if S[0] == S[1]:
    if S[0] != S[2] and S[2] == S[3]:
        print("Yes")
    else:
        print("No")
elif S[0] == S[2]:
    if S[0] != S[1] and S[1] == S[3]:
        print("Yes")
    else:
        print("No")
elif S[0] == S[3]:
    if S[0] != S[1] and S[1] == S[2]:
        print("Yes")
    else:
        print("No")
else:
    print("No")


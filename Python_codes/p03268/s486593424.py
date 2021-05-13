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
INF =  float("inf")
import bisect

N, K = list(map(int, input().split()))

if K % 2 == 1:
    print((N // K)**3)
else:
    print(((N // (K //2)) - (N // K))** 3 + (N // K)**3)


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

N = int(input())
S = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = ""
for i in range(len(S)):
    for j in range(26):
        if S[i] == alphabet[j]:
            k = (j+N) % 26
            ans += alphabet[k]
            break

print(ans)


#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math
import re

sys.setrecursionlimit(1000000)

K = input()
A = map(int, raw_input().split())[::-1]

minN = 2
maxN = 2

for num in A:
    minN = (minN / num + (minN % num != 0)) * num
    maxN = maxN / num * num + num - 1
    if maxN < minN:
        print -1
        exit()

print minN, maxN
import sys
import numpy as np
import math
import collections
import copy
from collections import deque 
from functools import reduce
from itertools import product

# input = sys.stdin.readline
S = input()
total = 0
for p in (product((0, 1), repeat=len(S)-1)):
    ns = S[0]
    for i, pp in enumerate(p, 1):
        if pp == 0:
            ns += S[i]
        else:
            total += int(ns)
            ns = S[i]
    total += int(ns)
print(total)




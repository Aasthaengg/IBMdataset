#BBBBBBBBBBB

import sys
import math
import itertools
import collections
import heapq
import numpy as np

rl = sys.stdin.readline

t = rl()
li = []
for i in range(len(t)):
    if t[i] == '?':
        li.append('D')
    else:
        li.append(t[i])
print(''.join(li))
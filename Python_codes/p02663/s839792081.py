#AAAAAAAAAAA

import sys
import math
import itertools
import collections
import heapq
import numpy as np

rl = sys.stdin.readline

h1, m1, h2, m2, k = map(int, rl().split())
m = h2*60 + m2 - h1*60 - m1
print(m-k)


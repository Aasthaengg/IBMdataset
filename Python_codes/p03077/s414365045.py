import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
ABCDE = [A, B, C, D, E]
print(-(-N//min(ABCDE)) + 4)

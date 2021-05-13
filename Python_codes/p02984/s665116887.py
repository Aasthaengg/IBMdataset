# -*- coding: utf-8 -*-
import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


mod = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))
rain = [0] * N


rain[0] = sum(A[::2]) - sum(A[1::2])
for i in range(1, N):
    rain[i] = 2*A[i-1] - rain[i-1]
print(*rain)

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
box = [0] * (N+1)
ans = []
for i in reversed(range(1, N+1)):
    # iの倍数の箱の合計
    if sum(box[i::i]) % 2 != A[i-1]:
        # sum_ = sum([box[i*j] for j in range(1, N//i+1)])
        box[i] = 1
        ans.append(i)
print(len(ans))
print(*ans)

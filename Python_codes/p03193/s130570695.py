# -*- coding: utf-8 -*-
import sys
from time import time, sleep
from random import random
from bisect import bisect, bisect_left
def inpl(): return list(map(int, input().split()))
N, H, W = inpl()
cnt = 0
for _ in range(N):
    a, b = inpl()
    if a>=H and b>=W:
        cnt += 1
print(cnt)
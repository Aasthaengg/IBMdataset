import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

k = int(input())


import queue
q = queue.Queue()

for i in range(1, 10):
    q.put(i)

if k <= 9:
    print(k)
    exit()

total = 9
while total <= k:
    x = q.get()
    if x % 10 != 0:
        val = x * 10 + x % 10 - 1
        q.put(val)
        total += 1
        if total == k:
            print(val)
            exit()

    val = x * 10 + x % 10
    q.put(val)
    total += 1
    if total == k:
        print(val)
        exit()
    if x % 10 < 9:
        val = x * 10 + x % 10 + 1
        q.put(val)
        total += 1
        if total == k:
            print(val)
            exit()
    
    if total >= k:
        for i in range(total - k):
            q.get()
        print(q.get())
        exit()

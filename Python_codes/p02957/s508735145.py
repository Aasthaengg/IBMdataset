import sys, heapq, bisect, math, fractions
from collections import deque

A, B = map(int, input().split())

if (A + B) % 2 == 0:
    print((A + B) // 2)
else:
    print("IMPOSSIBLE")
import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

r, g, b = map(int, input().split())
K = int(input())

while K > 0 and r >= g:
    g *= 2
    K -= 1
while K > 0 and g >= b:
    b *= 2
    K -= 1

if g > r and b > g:
    print("Yes")
else:
    print("No")

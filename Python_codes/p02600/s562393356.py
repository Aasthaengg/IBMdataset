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

x = int(input())

if x >= 1800:
    print(1)
elif x >= 1600:
    print(2)
elif x >= 1400:
    print(3)
elif x >= 1200:
    print(4)
elif x >= 1000:
    print(5)
elif x >= 800:
    print(6)
elif x >= 600:
    print(7)
elif x >= 400:
    print(8)

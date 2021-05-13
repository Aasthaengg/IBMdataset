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

S = input()
S = S[::-1]

a = "dream"
b = "dreamer"
c = "erase"
d = "eraser"

while len(S) > 0:
    if S[:5] == a[::-1] or S[:5] == c[::-1]:
        S = S[5:]
    elif S[:6] == d[::-1]:
        S = S[6:]
    elif S[:7] == b[::-1]:
        S = S[7:]
    else:
        print("NO")
        exit()
print("YES")



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

S = [0] * 3
S[0] = input()
S[1] = input()
S[2] = input()

cur = 0
while True:
    if len(S[cur]) > 0:
        nx = ord(S[cur][0]) - ord('a')
        S[cur] = S[cur][1:]
        cur = nx
    else:
        print(chr(ord('A') + cur))
        break


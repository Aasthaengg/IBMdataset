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

A, B, C = sorted(map(int, input().split()))

ans = 0
if C % 2 == 0:
    if A % 2 == 0 and B % 2 == 1:
        ans += 1
        A += 1
        C += 1
    elif A % 2 == 1 and B % 2 == 0:
        ans += 1
        B += 1
        C += 1
    elif A % 2 == 1 and B % 2 == 1:
        ans += 1
        A += 1
        B += 1
else:
    if A % 2 == 0 and B % 2 == 1:
        ans += 1
        B += 1
        C += 1
    elif A % 2 == 1 and B % 2 == 0:
        ans += 1
        A += 1
        C += 1
    elif A % 2 == 0 and B % 2 == 0:
        ans += 1
        A += 1
        B += 1

while C > A:
    A += 2
    ans += 1

while C > B:
    B += 2
    ans += 1

print(ans)
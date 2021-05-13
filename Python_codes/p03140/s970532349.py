import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N = int(input())
a = input()
b = input()
c = input()

ans = 0
for i in range(N):
    cost = INF
    for w in range(26):
        now = 0
        if ord(a[i]) != (w + ord('a')):
            now += 1
        if ord(b[i]) != (w + ord('a')):
            now += 1
        if ord(c[i]) != (w + ord('a')):
            now += 1
        cost = min(now, cost)
    ans += cost
print(ans)
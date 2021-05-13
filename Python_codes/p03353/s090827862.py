from collections import defaultdict, Counter, namedtuple, deque
import itertools
import functools
import bisect
import heapq
import math
from fractions import gcd

NN = 202020
MOD = 10**9+7
INF = float("inf")

s = input()
k = int(input())
strings = set()

for i in range(len(s)):
    for j in range(5):
        end = i+j+1
        if end > len(s):
            break
        strings.add(s[i:end])

strings = sorted(list(strings))
# print(strings)

print(strings[k-1])

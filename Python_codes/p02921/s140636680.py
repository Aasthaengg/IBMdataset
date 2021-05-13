import sys
from math import ceil, floor, sqrt, sin, cos, pi
from itertools import accumulate, permutations, combinations
from fractions import gcd # 最大公約数
from collections import deque, Counter
from operator import itemgetter
from heapq import heappop,heappush
sys.setrecursionlimit(10**7)
def lcm(x, y): return ((x * y) // gcd(x, y)) # 最小公倍数
# list(map(int, input().split()))
s = input()
t = input()

ans = 0
for i in range(3):
    if s[i] == t[i]: ans += 1
print(ans)
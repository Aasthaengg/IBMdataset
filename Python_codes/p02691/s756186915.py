import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
import bisect
import numpy as np
import math
from collections import deque
from collections import defaultdict
from math import gcd

N = int(input())
A = list(map(int, input().split()))
left = defaultdict(int)
right = defaultdict(int)
for i in range(N):
    num = i + 1
    left[A[i]+num] += 1
    right[-A[i]+num] += 1

ans = 0
for k, v in left.items():

    ans += right[k]*v

print(ans)
import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())

def f(n):
    if n < 2:
        return 1
    else:
        return n * f(n - 2)

if N % 2 == 1:
    print(0)
else:
    ans = 0
    x = 5
    while x * 2 <= N:
        ans += N // (x * 2)
        x *= 5
    print(ans)

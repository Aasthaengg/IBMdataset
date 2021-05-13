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

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

def fib(n):
    if dp[n] > 0:
        return dp[n]
    
    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]

print(fib(N))
    

import math
import sys
import queue
from collections import Counter
from itertools import accumulate
from fractions import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def combination_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

mod = 1000000007

"""
# 標準入力取得
## 文字列
    = sys.stdin.readline().rstrip()
    = list(sys.stdin.readline().rstrip())

## 数値
    = int(sys.stdin.readline())
    = map(int, sys.stdin.readline().split())
    = list(map(int, sys.stdin.readline().split()))
    = [list(map(int,list(sys.stdin.readline().split()))) for i in range(N)]
"""

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    if N % K == 0:
        print(0)
    else:
        print(1)
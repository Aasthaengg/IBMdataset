from fractions import gcd
from functools import reduce

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
N, M, *A = map(int, read().split())
 
# 「奇数倍」に帰着
A = [x >> 1 for x in A]
 

def merge(a, b):
    g = gcd(a, b)
    a //= g
    b //= g
    if a % 2 == 0:
        return 0
    if b % 2 == 0:
        return 0
    n = a * b * g
    if n > 10 ** 9:
        return 0
    return n


x = reduce(merge, A)

if x == 0:
    answer = 0
else:
    answer = (M//x) - (M//(x+x))
 
print(answer)

import math
import collections
import fractions
import itertools
import functools
import  operator

def solve():
    n = int(input())
    p = 1
    mod = 10**9+7
    for i in range(1,n+1):
        p *= i
        p %= mod
    print(p)
    return 0

if __name__ == "__main__":
    solve()

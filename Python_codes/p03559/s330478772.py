# -*- coding: utf-8 -*-
import sys
import math
import os
import itertools
import string
import heapq
from _collections import defaultdict
from functools import lru_cache
import bisect

class Scanner():
    def int():
        return int(sys.stdin.readline().rstrip())
    def string():
        return sys.stdin.readline().rstrip()
    def map_int():
        return [int(x) for x in Scanner.string().split()]
    def string_list(n):
        return [input() for i in range(n)]
    def int_list_list(n):
        return [Scanner.mapInt() for i in range(n)]
    def int_cols_list(n):
        return [int(input()) for i in range(n)]
        
class Math():
    def gcd(a,b):
        if b == 0:
            return a
        return Math.gcd(b,a % b)
    def lcm(a,b):
        return (a * b) // Math.gcd(a,b)
    def roundUp(a,b):
        return -(-a // b)
    def toUpperMultiple(a,x):
        return Math.roundUp(a,x) * x
    def toLowerMultiple(a,x):
        return (a // x) * x
    def nearPow2(n):
        if n <= 0:
            return 0
        if n & (n - 1) == 0:
            return n
        ret = 1
        while(n > 0):
            ret <<= 1
            n >>= 1
        return ret
    def isPrime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        d = int(n ** 0.5) + 1
        for i in range(3,d + 1,2):
            if n % i == 0:
                return False
        return True

MOD = int(1e09) + 7

def main():
    N = Scanner.int()
    A = Scanner.map_int()
    B = Scanner.map_int()
    C = Scanner.map_int()
    A.sort()
    B.sort()
    C.sort()
    ans = 0
    for i in range(N):
        n,m = 0,0
        n = bisect.bisect_left(A,B[i])
        m = N - bisect.bisect_right(C,B[i])
        ans += n * m
    print(ans)
    return

if __name__ == "__main__":
    main()

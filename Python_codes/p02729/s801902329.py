#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
n, m = [int(x) for x in input().split()]
def c2(n):
    return n * (n - 1) // 2
print(c2(n) + c2(m))
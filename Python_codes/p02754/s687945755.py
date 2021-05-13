#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
n, a, b = [int(x) for x in input().split()]
print(a * (n // (a + b)) + min(a, n % (a + b)))
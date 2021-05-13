#!/usr/bin/env python3
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c = map(int,readline().split())
print(min(a + b, b + c, c + a))
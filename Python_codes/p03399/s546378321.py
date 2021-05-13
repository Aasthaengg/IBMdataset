#!/usr/bin/env python3
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c, d =  [int(readline()) for i in range(4)]
print(min(a + c, a + d, b + c, b + d))
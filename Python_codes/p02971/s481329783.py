#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
a = sorted((int(input()), i) for i in range(n))
for i in range(n):
    print(a[-1][0] if i != a[-1][1] else a[-2][0])

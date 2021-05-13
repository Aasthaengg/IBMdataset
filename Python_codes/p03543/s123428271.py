#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


N = input()

good = [str(i)*3 for i in range(10)]

flag = "No"
for num in good:
    if num in N:
        flag = "Yes"

print(flag)

#!/usr/bin/env python3

import sys
from math import factorial
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)


N = int(input())

if N % 2:
    print(0)
    sys.exit()


div = 10
count = 0
while N // div:
    count += N // div
    div *= 5


print(count)




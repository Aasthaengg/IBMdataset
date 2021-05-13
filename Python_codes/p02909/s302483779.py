#!/usr/bin/env python3

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

S = input()

if S == "Sunny":
    print("Cloudy")
elif S == "Cloudy":
    print("Rainy")
else:
    print("Sunny")


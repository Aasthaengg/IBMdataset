#!/usr/bin/env python3
import sys
input = sys.stdin.readline
import math

a, b, c = map(int, input().split())
if c - a - b < 0:
    print("No")
    exit()
if a * b * 4 < (c - a - b)**2:
    print("Yes")
else:
    print("No")

#!/usr/bin/env python3
import sys
input = sys.stdin.readline

m1, d1 = [int(item) for item in input().split()]
m2, d2 = [int(item) for item in input().split()]
if d2 == 1:
    print(1)
else:
    print(0)
#!/usr/bin/python3
import sys
input = lambda: sys.stdin.readline().strip()
n, d = [int(x) for x in input().split()]
l = 2 * d + 1
print((n + l - 1) // l)
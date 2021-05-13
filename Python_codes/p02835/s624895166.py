#!/usr/bin/env python3
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

A,B,C = map(int,readline().rstrip().split())
if (A+B+C) <=21:
    print("win")
else:
    print("bust")
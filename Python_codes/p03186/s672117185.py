# A
import sys

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip() # ignore trailing spaces


A,B,C = na()


if A+B >= C-1:
    print(B+C)
else:
    print(B+B+A+1)







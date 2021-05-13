import numpy as np
import sys

input = sys.stdin.readline

A,B,C ,K= map(int,input().split())


if K%2 == 1 and abs(B-A) < 1000000000000000000:
    print(B-A)
elif  K%2 == 0 and abs(A-B) < 1000000000000000000:
    print(A-B)
else:
    print("Unfair")


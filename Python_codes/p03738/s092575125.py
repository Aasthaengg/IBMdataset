import numpy as np
import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
if A > B:
    print("GREATER")
elif A < B:
    print("LESS")
else:
    print("EQUAL")
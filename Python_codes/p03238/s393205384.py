import sys
import numpy as np
input = sys.stdin.readline
N = int(input())
if N == 2:
    A = []
    for _ in range(2):
        A.append(int(input()))
    print(sum(A))
else:
    print("Hello World")
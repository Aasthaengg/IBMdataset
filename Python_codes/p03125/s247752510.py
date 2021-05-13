import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
if B%A == 0:
    print(A+B)
else:
    print(B-A)
import sys
import math
from collections import deque


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
A = instrl()

B = deque()

if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            B.append(A[i])
        else:
            B.insert(0,A[i])
else:
    for i in range(n):
        if i % 2 == 0:
            B.insert(0,A[i])
        else:
            B.append(A[i])

print(" ".join(B))
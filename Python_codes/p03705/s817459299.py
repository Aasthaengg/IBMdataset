import sys
input = sys.stdin.readline
from collections import *

N, A, B = map(int, input().split())

if A>B:
    print(0)
    exit()
    
m = B+A*(N-1)
M = A+B*(N-1)
print(max(0, M-m+1))
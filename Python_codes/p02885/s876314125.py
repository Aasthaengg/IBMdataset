import sys
input = sys.stdin.readline
from collections import *

A, B = map(int, input().split())
print(max(A-2*B, 0))
import sys
import math
import numpy as np
input = sys.stdin.readline
A, B = [int(x) for x in input().split()]
print(max(A+B, A*B, A-B))

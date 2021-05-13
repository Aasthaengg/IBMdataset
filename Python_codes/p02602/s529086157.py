import sys
import numpy as np
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

B = 0
s = 1
for i, a in enumerate(A):
    if i >= K:
        B = A[i-K]
        s = a
        if B != 0 and B < s:
            print('Yes')
        elif B != 0 and B >= s:
            print('No')

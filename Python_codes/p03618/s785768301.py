import sys
#import numpy as np
from collections import Counter

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to numbers only
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

A = list(rs())
answer = 1
c = Counter(A)
for i in range(len(A)):
    answer += len(A) - i - c[A[i]]
    c[A[i]] -= 1

print(answer)
# 53
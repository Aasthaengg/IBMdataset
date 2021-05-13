import sys
import numpy as np

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, T = rl()
A = np.array(rl())
A_cummin = np.minimum.accumulate(A)
B = A - A_cummin

answer = (B == B.max()).sum()
print(answer)
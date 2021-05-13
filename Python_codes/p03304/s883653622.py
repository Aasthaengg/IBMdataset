import sys
import numpy as np

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to numbers only
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, M, D = rl()
if D == 0:
    print((M-1) / N)
else:
    answer = 2 * (N-D) * (M-1) / N**2
    print(answer)
# 49
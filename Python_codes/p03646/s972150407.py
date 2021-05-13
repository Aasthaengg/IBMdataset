import sys
import numpy as np

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to only numbers
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

K = ri()
A = np.ones(50, dtype=np.int64)
A *= 49
x, y = divmod(K, 50)
A += x
A[:y] += 50 - (y-1)
A[y:] -= y
print(50)
print(*A)
# 59
import sys
import numpy as np
n = int(input())
s = np.array([int(input()) for _ in range(n)])
if len(s[s % 10 == 0]) == n:
    print(0)
    sys.exit()
if s.sum() % 10:
    print(int(s.sum()))
else:
    t = s[~(s % 10 == 0)].min()
    print(int(s.sum() - t))
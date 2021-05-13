import numpy as np
import math

N = int(input())
A = np.array(list(map(int, input().split())))

base = np.arange(N, dtype=int) + 1
tmp = A - base
b = math.floor(np.median(tmp))
ans = np.abs(tmp - b).sum()
print(ans)
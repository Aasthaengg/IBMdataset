import sys
import numpy as np
from itertools import permutations

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = np.array(readline().split(), np.int64)
b = np.array(readline().split(), np.int64)

n_lst = [i for i in range(1, n+1)]
per_lst = list(permutations(n_lst, n))

ans = abs((per_lst.index(tuple(a))+1) - (per_lst.index(tuple(b))+1))

print(ans)

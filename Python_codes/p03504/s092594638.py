import sys
import numpy as np
read = sys.stdin.read

N, C, *stc = map(int, read().split())
recoder = np.zeros((C + 1, 10 ** 5 + 1), np.int64)

for s, t, c in zip(*[iter(stc)] * 3):
    recoder[c, s - 1:t] = 1

answer = np.cumsum(recoder, axis=0).max()

print(answer)
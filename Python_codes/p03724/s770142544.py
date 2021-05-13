import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

nums = np.array(read().split(), np.int32)[2:]

cond = np.all(np.bincount(nums) % 2 == 0)
print('YES' if cond else 'NO')
import sys
import numpy as np


read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
nums = np.array(read().split(), np.int32)[2:]
flg = np.all(np.bincount(nums) % 2 == 0)
if flg:
    print('YES')
else:
    print('NO')

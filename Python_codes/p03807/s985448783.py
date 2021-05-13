import numpy as np

n = int(input())
a = np.array(input().split(), np.int64)

if np.count_nonzero(a % 2 == 1) % 2 == 1:
    print('NO')
else:
    print('YES')

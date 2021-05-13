import numpy as np
import math
N, K = map(int, input().split())
aaa = np.array(list(map(float, input().split())), dtype='f8')
l = 0
r = 10 ** 9
while r != l:
    mid = (r + l) // 2
    bbb = aaa / mid
    bbb -= 1
    bbb = np.ceil(bbb)
    if bbb.sum() <= K:
        r = mid
    else:
        l = mid + 1
print(l)

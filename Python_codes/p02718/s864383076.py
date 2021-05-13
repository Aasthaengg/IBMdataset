import numpy as np
n,m = map(int, input().split())
a = np.array([int(i) for i in input().split()])
ans = (a >= a.sum()/(4*m)).sum()
if ans >= m:
    print('Yes')
else:
    print('No')
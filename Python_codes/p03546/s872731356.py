import numpy as np
import scipy.sparse as sps
import sys,math

h,w = map(int,input().split())
c = np.array([list(map(int,input().split()))for i in range(10)])
wf = sps.csgraph.floyd_warshall(c,directed=1).astype(int)

a = np.array([list(map(int,input().split()))for i in range(h)])

ans = 0
for arr in a:
    for num in arr:
        if num == -1: continue
        else: ans += wf[num][1]
print(ans)


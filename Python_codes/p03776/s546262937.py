import os
import sys

import numpy as np
from scipy.misc import comb

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N, A, B = list(map(int, sys.stdin.readline().split()))
V = list(map(int, sys.stdin.readline().split()))

V.sort(reverse=True)
V = np.array(V)
cs = V.cumsum()
averages = cs / (np.arange(N) + 1)

# 最大の平均
max_average = averages[A - 1:B].max()
# 選ぶべき数
count = averages[A - 1:B].argmax() + A

# しきい値になってるのが何個あるか
threshold = V[count - 1]
threshold_cnt = (V == threshold).sum()

print(float(max_average))
if np.all(V[:count] == V[0]):
    # しきい値 t 個のとき、tCa + tC(a+1) + ... + tCb
    ans = 0
    for r in range(A, B + 1):
        ans += comb(threshold_cnt, r, exact=True)
    print(ans)
else:
    gt_cnt = (V > threshold).sum()
    print(comb(threshold_cnt, count - gt_cnt, exact=True))

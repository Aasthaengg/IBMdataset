import sys
import numpy as np
read = sys.stdin.read

N, A, B, *h = map(int, read().split())

h = np.array(h, np.int64)

# 2部探索する。n回の爆発で魔物をすべて倒せるか否や
l = 0
r = max(h) // B + 2
a = A - B
while l + 1 < r:
    mid = (l + r) // 2
    w = B * mid
    tmp = h - w
    tmp = tmp[tmp > 0]
    tmp = tmp // a + np.minimum(tmp % a, 1)
    if tmp.sum() <= mid:
        r = mid
    else:
        l = mid

print(r)
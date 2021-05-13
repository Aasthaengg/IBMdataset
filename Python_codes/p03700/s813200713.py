import numpy as np

n, a, b = map(int, input().split())
h = np.array([int(input()) for _ in range(n)], dtype=np.int64)


def f(x):
    li = h - b * x
    li[li < 0] = 0
    cnt = np.ceil(li / (a - b))
    ret = cnt.sum() <= x
    return ret


l = 0
r = np.ceil(max(h) / b).astype(np.int64)
while r - l > 1:
    mid = (l + r) // 2
    if f(mid):
        r = mid
    else:
        l = mid

print(r)

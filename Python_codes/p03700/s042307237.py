import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, A, B = lr()
A -= B # 全員にBのダメージが加わるとする
H = np.array([ir() for _ in range(N)])

def check(x):
    hp = H - B*x
    hp = hp[hp>0]
    cnt = ((hp + A - 1) // A).sum()
    return cnt <= x

#二分探索
left = 0 #NG
right = 10 ** 9 #OK
while right > left + 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
# 45
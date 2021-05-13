import sys
import numpy as np

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to numbers only
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, M = rl()
A = np.array(rl())
A.sort()

def shake_cnt(x):
    # x以上の幸福度の時、何回握手するかを返す
    # Xは握手しない人の数
    X = np.searchsorted(A, x-A)
    return N * N - X.sum()

right = 10 ** 6 #M回未満
left = 0 # M回以上
while right > left + 1:
    mid = (right+left) // 2
    if shake_cnt(mid) >= M:
        left = mid
    else:
        right = mid

# right以上の幸福度の場合はまず握手して、ちょうどleftの幸福度で人数調整
Acum = np.zeros(N+1, dtype=np.int64)
Acum[1:] = A.cumsum()
Y = np.searchsorted(A, right-A)
happy = (Acum[-1] - Acum[Y]).sum() + (A * (N-Y)).sum()
happy += left * (M-shake_cnt(right))
print(happy)

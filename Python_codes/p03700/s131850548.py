import numpy as np

N, A, B = map(int, input().split())
A -= B
H = np.array([int(input()) for _ in range(N)], dtype=np.int64)


def C(X):
    """
    x回爆発して、全部消滅させれるとTrue
    """
    HP = H - X * B
    HP = HP[HP > 0]
    cnt = (HP + A - 1) // A
    return cnt.sum() <= X


l = -1
r = 10 ** 18
while r - l > 1:
    m = (r + l) // 2
    if C(m):
        r = m
    else:
        l = m

ans = r
print(ans)

import numpy as np
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

N, A, B = map(int, readline().split())
A = A - B
H = np.array([int(readline()) for _ in range(N)], dtype=np.int64)


def C(T):
    h = H-B*T
    h = h[h > 0]
    bomb = (h + A - 1) // A
    return bomb.sum() <= T


left = 0
right = 10 ** 18
while right - left > 1:
    mid = (right + left) // 2
    if C(mid):
        right = mid
    else:
        left = mid

ans = right
print(ans)

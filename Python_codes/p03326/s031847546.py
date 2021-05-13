from itertools import product
import numpy as np
N, M = map(int, input().split())
XYZ = [list(map(int, input().split())) for _ in range(N)]
X, Y, Z = np.array(XYZ, dtype=np.int64).T

if M == 0:
    print(0)
    exit()

ans = -10 ** 18
for p in product([-1, 1], repeat=3):
    xyz = X * p[0] + Y * p[1] + Z * p[2]
    xyz.sort()
    ans = max(ans, xyz[-M:].sum())
print(ans)
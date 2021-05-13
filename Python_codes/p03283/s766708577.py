N, M, Q = map(int, input().split())
import numpy as np
LR = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, M+1):
    l, r = map(int, input().split())
    LR[l][r] += 1
cLR = np.cumsum(np.cumsum(LR, axis=0), axis=1)

for _ in range(Q):
    p, q = map(int, input().split())
    ans = cLR[N][q] - cLR[p-1][q]
    print(ans)
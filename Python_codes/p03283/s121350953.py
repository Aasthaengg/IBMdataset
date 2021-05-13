N, M, Q = map(int, input().split())
wa = [[0]*(N+1) for _ in range(N+1)]
import numpy as np

for _ in range(M):
    l, r = map(int, input().split())
    wa[l][r] += 1

cwa = np.cumsum(np.cumsum(wa, axis=0), axis=1).tolist()
for i in range(Q):
    p, q = map(int, input().split())
    ans = cwa[N][q]-cwa[p-1][q]
    print(ans)

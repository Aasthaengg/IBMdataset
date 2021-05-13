import numpy as np

N, K = map(int, input().split())
hs = np.array(list(map(int, input().split())))

a = np.zeros(N, int)
a[0] = 0
a[1] = abs(hs[1] - hs[0])

if N == 2:
    print(a[-1])
else:
    for i in range(2, N):
        b = a[max(i-K,0):i] + np.abs(hs[i] - hs[max(i-K,0):i])
        a[i] = np.min(b)
    print(a[-1])
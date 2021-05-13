import numpy as np
n, k = map(int, input().split())
P = list(map(int, input().split()))
P = list(map(lambda x: (x + 1) * x / 2 / x, P))
P = np.array([0] + P)
P = np.cumsum(P)
ans = np.zeros(n - (k - 1))
for i in range(n - (k - 1)):
    ans[i] = P[k + i] - P[i]
print(np.max(ans))
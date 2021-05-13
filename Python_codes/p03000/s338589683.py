import numpy as np

n, x = map(int, input().split())
L = list(map(int, input().split()))

CS_L = np.cumsum(L).tolist()
ans = len([l for l in CS_L if l <= x])
print(ans + 1)
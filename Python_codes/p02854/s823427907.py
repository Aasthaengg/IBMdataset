import numpy as np

N = int(input())
A = [0] + list(map(int, input().split()))

cumsum = np.cumsum(A)

ans = float("inf")
for i in range(1, N):
    left = cumsum[i]
    right = cumsum[-1] - cumsum[i]
    tmp = abs(right - left)
    if tmp < ans:
        ans = tmp

print(ans)

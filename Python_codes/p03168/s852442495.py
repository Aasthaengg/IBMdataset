import numpy as np

N = int(input())
P = list(map(float, input().split()))
DP = np.zeros(N+2)
DP[0] = 1
for i, p in enumerate(P, 1):
    DP = DP * (1 - p) + np.roll(DP, 1) * p

print(np.sum(DP[N//2 + 1:]))
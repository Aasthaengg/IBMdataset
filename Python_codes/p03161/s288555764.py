import math

N, K = map(int, input().split())
h = [0] + list(map(int, input().split()))

DP = [math.inf] * (N+1)

for i in range(1, N+1):
    if i == 1:
        DP[i] = 0
        continue
    if i == 2:
        DP[i] = abs(h[1] - h[2])
        continue
    for j in range(1, min(i, K) + 1):
        DP[i] = min(DP[i], DP[i-j] + abs(h[i-j] - h[i]))


print(DP[N])


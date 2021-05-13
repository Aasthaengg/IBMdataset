import math
N, K = map(int, input().split())
p = 0
if N >= K:
    p += N - K + 1
    for r in range(1, K):
        p += (1 / 2) ** math.ceil(math.log2(K / r))
else:
    for r in range(1, N + 1):
        p += (1 / 2) ** math.ceil(math.log2(K / r))
print(p / N)
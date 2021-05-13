import math
N, K = map(int, input().split())
p = [0] * N
for i in range(N):
    n = i + 1
    x = 1 / N
    while n < K:
        x *= 0.5
        n *= 2
    p[i] = x
ans = math.fsum(p)
print(ans)
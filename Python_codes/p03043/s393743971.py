import math
N, K = map(int, input().split())

ans = 0
for r in range(1, min(K, N+1)):
    x = math.ceil( math.log2(K/r))
    ans += pow(0.5, x) / N
    # print(x, pow(0.5, x) / N)
if K <= N:
    ans += (N - K + 1) / N
print(ans)

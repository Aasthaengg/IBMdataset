
from os import readlink


K, N = map(int, input().split())
X = list(map(int, input().split()))

ans = K - (X[0] + K - X[-1])
for i in range(1, N):
    ans = min(ans, K - (X[i] - X[i - 1]))
print(ans)

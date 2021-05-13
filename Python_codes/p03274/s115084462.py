import sys
import bisect
input = sys.stdin.buffer.readline


N, K = map(int, input().split())
X = list(map(int, input().split()))

orient = bisect.bisect_left(X, 0)
X_posi = [float('inf')] * N
X_nega = [float('inf')] * N

for i in range(N-orient):
    X_posi[i] = X[orient+i]

for i in range(orient):
    X_nega[i] = -X[orient - i - 1]

ans = float('inf')
for i in range(K+1):
    if i == 0:
        ans = min(X_nega[K-i-1], ans)
    elif i == K:
        ans = min(X_posi[i-1], ans)
    else:
        ans = min(ans, X_posi[i-1] + X_nega[K-i-1] + min(X_posi[i-1], X_nega[K-i-1]))
print(ans)

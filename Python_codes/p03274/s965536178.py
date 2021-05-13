N, K = map(int, input().split())
X = list(map(int, input().split()))
ans = float("inf")
for i in range(N - K + 1):
    left, right = X[i], X[i + K - 1]
    dist = right - left
    ans = min(ans, abs(left) + dist, abs(right) + dist)
print(ans)

N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 10**18
for i in range(N - K + 1):
    x1 = X[i]
    x2 = X[i + K - 1]
    if x1 * x2 >= 0:
        dist = max(abs(x1), abs(x2))
    else:
        dist = min(abs(x1), abs(x2)) + abs(x1 - x2)
    ans = min(ans, dist)
print(ans)

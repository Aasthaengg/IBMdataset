N, K = map(int, input().split())
X = tuple(map(int, input().split()))
print(min(X[i + K - 1] - X[i] + min(abs(X[i]), abs(X[i + K - 1])) for i in range(N - K + 1)))
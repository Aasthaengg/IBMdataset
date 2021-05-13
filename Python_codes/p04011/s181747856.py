N, K, X, Y = map(int, open(0).read().split())
print(X*min(N, K)+Y*max(N-K, 0))

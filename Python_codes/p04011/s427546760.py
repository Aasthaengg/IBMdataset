N, K, X, Y = [int(input()) for _ in range(4)]
print(K * X + (N - K) * Y if N >= K else N * X)

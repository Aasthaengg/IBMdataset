N, K, X, Y = [int(input()) for _ in range(4)]
m = min(N, K)
print(X * m + Y * (N - m))
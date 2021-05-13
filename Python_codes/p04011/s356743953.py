N, K, X, Y = [int(input()) for _ in range(4)]
res = N * X
if N > K:
    res += (N - K) * (Y - X)
print(res)
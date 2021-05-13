N, K, X, Y = (int(input()) for _ in range(4))
result = 0
if K >= N:
    result = N * X
else:
    result = K * X + ((N - K) * Y)
print(result)

N, M, D = map(int, input().split())
print(2 * (N - D) * (M - 1) / (N ** 2) if D else (M - 1) / N)

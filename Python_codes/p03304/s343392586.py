N, M, D = map(int, input().split())
if D == 0:
    print((M - 1) / N)
else:
    print((N - D) * (M - 1) * 2 / (N ** 2))
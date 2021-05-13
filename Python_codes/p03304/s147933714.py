N, M, D = map(int, input().split())

if D == 0:
    print((M - 1) * (max(0, N - D)) / (N ** 2))
else:
    print((M - 1) * 2 * (max(0, N - D)) / (N ** 2))
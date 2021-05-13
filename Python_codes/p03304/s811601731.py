N, M, D = map(int, input().split())
if D == 0:
    p = (1 / N) * (M - 1)
else:
    p = (2 * (N - D) / (N ** 2)) * (M - 1)

print(p)

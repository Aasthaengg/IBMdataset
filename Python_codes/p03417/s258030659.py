N, M = sorted(map(int, input().split()))
print(0 if 2 in [N, M] else abs(M - 2) if N == 1 else (N - 2) * (M - 2))

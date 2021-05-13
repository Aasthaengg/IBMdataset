N, K, S = map(int, input().split())
A = [S] * K + [S - 1 if S > 2 else 100] * (N-K)
print(*A)

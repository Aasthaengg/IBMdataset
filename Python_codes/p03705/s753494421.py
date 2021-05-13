N, A, B = map(int, input().split())
print(0 if N == 1 and A != B else max(0, max(0, N - 2) * (B - A) + 1))
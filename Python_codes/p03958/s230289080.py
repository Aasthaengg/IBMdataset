K, T = map(int, input().split())
A = sorted(map(int, input().split()))

print(max(A[-1] - sum(A[:-1]) - 1, 0))

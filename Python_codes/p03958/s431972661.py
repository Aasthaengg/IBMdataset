
K, T = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

print(max(0, A[0] - 1 - sum(A[1:])))
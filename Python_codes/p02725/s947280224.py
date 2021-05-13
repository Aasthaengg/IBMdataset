K, N = map(int, input().split())

A = list(map(int, input().split()))
A. sort()

print(min(K - (A[i] - A[i-1])%K for i in range(N)))
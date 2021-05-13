N, K = map(int, input().split())
A = tuple(map(int, input().split()))
for i in range(N - K): print('Yes' if A[K + i] > A[i] else 'No')
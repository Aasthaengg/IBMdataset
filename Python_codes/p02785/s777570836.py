N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()

SUM = 0
for i in range(N - K):
    SUM += A[i]

print(SUM)
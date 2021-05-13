N = int(input())
B = list(map(int, input().split()))

A = [None] * N
A[0] = B[0]
A[-1] = B[-1]

for i in range(1, len(B)):
    A[i] = min(B[i], B[i - 1])

print(sum(A))

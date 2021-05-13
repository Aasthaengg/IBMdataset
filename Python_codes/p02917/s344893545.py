N = int(input())
B = list(map(int, input().split()))

ans = 0

A = [0] * N
A[0] = B[0]
A[-1] = B[-1]

for i in range(1, N-1):
    min_B = min(B[i-1], B[i])
    A[i] = min_B

print(sum(A))

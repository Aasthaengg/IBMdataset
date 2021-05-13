N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

C = [0] * N

for i in range(N):
    x = min(A[i], B[i])
    y = min(A[i + 1], max(B[i] - A[i], 0))
    C[i] = x + y
    A[i] = A[i] - x
    A[i + 1] = A[i + 1] - y

print(sum(C))
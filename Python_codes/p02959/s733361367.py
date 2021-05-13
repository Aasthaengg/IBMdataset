import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_orig = A.copy()

rest = 0
for i in range(N):
    A[i] -= B[i]
    if A[i] < 0:
        A[i+1] += A[i]
        A[i] = 0
        if A[i + 1] < 0:
            A[i+1] = 0

print(sum(A_orig)-sum(A))

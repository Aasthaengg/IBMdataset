import copy
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = copy.copy(A)
for i in range(N):
    if B[i] <= A[i]:
        A[i] -= B[i]
    elif B[i] <= A[i] + A[i + 1]:
        A[i + 1] -= B[i] - A[i]
        A[i] = 0
    else:
        A[i], A[i + 1] = 0, 0
C = [C[i] - A[i] for i in range(N + 1)]
print(sum(C))
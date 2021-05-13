N = int(input())

A = (int(x) for x in input().split())

A = list(A)

step = 0

for i in range(N-1):
    if A[i] - A[i+1] >= 0:
        step += A[i] - A[i+1]
        A[i+1] += A[i] - A[i+1]



print(step)
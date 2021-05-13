N = int(input())
A = [0]*(N+1)
if N == 0 or N == 1:
    print(1)
else:
    A[0] = 1
    A[1] = 1
    for i in range(2, N+1):
        A[i] = A[i-1] + A[i-2]
    print(A[N])

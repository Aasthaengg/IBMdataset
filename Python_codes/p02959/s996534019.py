N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
before = sum(A)
for i in range(N):
    if B[i] <= A[i]:
        A[i] -= B[i]
    else:
        r =  B[i] - A[i]
        A[i] = 0
        A[i+1] -= r
        if A[i+1] < 0:
            A[i+1] = 0
print(before - sum(A))





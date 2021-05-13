N = int(input())
A = list(map(int,input().split()))
H = 0
for i in range(1,N):
    if A[i] < A[i-1]:
        sa = A[i-1] - A[i]
        A[i] = A[i-1]
        H += sa
print(H)
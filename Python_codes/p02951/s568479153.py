A = list(map(int,input().split()))
if A[2] > A[0]-A[1]:
    print(A[2] - (A[0]-A[1]))
else:
    print(0)
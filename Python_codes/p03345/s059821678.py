A = list(map(int,input().split()))
if A[3] == 0:
    print(A[0]-A[1])
elif A[3]%2 == 0:
    print(A[0]-A[1])
else:
    print(A[1]-A[0])
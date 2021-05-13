A = list(map(int,input().split()))
if A[0] <= 5:
    print(0)
elif A[0]  <= 12:
    print(A[1]//2)
else:
    print(A[1])

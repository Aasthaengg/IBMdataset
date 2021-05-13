A=list(map(int,input().split()))

if A[0]==A[1] and not A[0]==A[2]:
    print(2)
elif not A[0]==A[1] and not A[1]==A[2] and not A[0]==A[2]:
    print(3)
elif A[0]==A[2] and not A[0]==A[1]:
    print(2)
elif A[1]==A[2] and not A[1]==A[0]:
    print(2)
else:
    print(1)

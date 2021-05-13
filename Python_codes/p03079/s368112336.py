A=[int(x) for x in input().split()]

A=sorted(A)

if A[0]==A[1] and A[0]==A[2]:
    print('Yes')
else:
    print('No')

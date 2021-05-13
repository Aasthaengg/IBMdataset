a,b,c=map(int,input().split())
A=[a,b,c]
A.sort()
k=A[0]+(A[2]-A[1])
if (A[2]-k)%2==0:
    print(A[2]-A[1]+(A[2]-k)//2)
else:
    print(A[2]-A[1]+(A[2]-k)//2+2)
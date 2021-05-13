N,M,X=map(int,input().split())
A=list(map(int,input().split()))
B=[]
C=[]
for i in range(M):
    if A[i]>X:
        B.append(A[i])
    elif A[i]<X:
        C.append(A[i])
print(min(len(B),len(C)))
def Binary_Search(A,x):
    L=0
    R=len(A)
    while R-L>1:
        C=(R+L-1)//2
        
        if A[C]<=x:
            L=C+1
        else:
            R=C+1
    return L
        
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

A.sort()
A.append(A[-1]+1)
B.sort()
C.sort()
C=[0]+C
C=[-c for c in C[::-1]]

S=0
for b in B:
    S+=Binary_Search(A,b-1)*Binary_Search(C,-(b+1))
print(S)

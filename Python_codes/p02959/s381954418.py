N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

before_sumA=sum(A)
before_sumB=sum(B)
for i in range(N):
    if A[i]>B[i]:
        R=A[i]
        A[i]-=B[i]
        B[i]=0
    elif A[i]==B[i]:
        R=A[i]
        A[i]=0
        B[i]=0
    elif A[i]+A[i+1]>B[i]:
        R=A[i]
        A[i]=0
        B[i]-=R
        A[i+1]-=B[i]
        B[i]=0
    else:
        R=A[i]+A[i+1]
        A[i]=0
        A[i+1]=0
        B[i]-=R

after_sumA=sum(A)
after_sumB=sum(B)
#print(before_sumA-after_sumA)
print(before_sumB-after_sumB)

N=int(input())
A=list(map(int,input().split()))

P=max(A)
I=A.index(P)
del A[I]
Q=min(A,key=lambda x:abs(2*x-P))
print(P,Q)
N=int(input())
A=[0]+list(map(int,input().split()))
B=[0]+list(map(int,input().split()))
C=[0]+list(map(int,input().split()))

X=0
for i in range(1,N+1):
    X+=B[i]

    if A[i-1]+1==A[i]:
        X+=C[A[i-1]]
print(X)
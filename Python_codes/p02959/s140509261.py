N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

S=0
for i in range(N):
    Y=min(A[i],B[i])
    S+=Y
    B[i]-=Y

    Z=min(A[i+1],B[i])
    A[i+1]-=Z
    S+=Z

print(S)

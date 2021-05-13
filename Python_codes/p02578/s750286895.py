N=int(input())
A=list(map(int,input().split()))
s=0
if N==1:
    print(0)
else:
    for i in range(N-1):
        if A[i+1]<A[i]:
            s=s+A[i]-A[i+1]
            A[i+1]=A[i]
    print(s)
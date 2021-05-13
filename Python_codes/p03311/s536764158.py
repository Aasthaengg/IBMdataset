N=int(input())
A=list(map(int,input().split()))

A=[A[i]-i-1 for i in range(0,N)]

A.sort()

if N%2==1:
    s=0
    for i in range(0,N):
        s=s+abs(A[i]-A[(N-1)//2])
    print(s)
else:
    s=0
    for i in range(0,N):
        s=s+abs(A[i]-A[N//2])
    print(s)

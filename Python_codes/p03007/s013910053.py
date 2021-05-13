N=int(input())
A=list(map(int,input().split()))
A.sort()
m=A[0]
if m>=0:
    M=sum(A)-2*m
    print(M)
    s=A[0]
    for i in range(0,N-1):
        if i!=N-2:
            print(s,A[i+1])
            s-=A[i+1]
        else:
            print(A[N-1],s)
else:
    if A[N-1]>0:
        start=0
        end=N-1
        while end-start>1:
            test=(end+start)//2
            if 0>A[test]:
                start=test
            else:
                end=test
        if 0>A[end]:
            mid=end
        else:
            mid=start
        M=sum(abs(A[i]) for i in range(0,N))
        print(M)
        s=A[0]
        for i in range(mid+1,N):
            if i!=N-1:
                print(s,A[i])
                s-=A[i]
            else:
                print(A[N-1],s)
                s=A[N-1]-s
        for i in range(1,mid+1):
            print(s,A[i])
            s-=A[i]
    else:
        M=-sum(A)+2*A[N-1]
        print(M)
        s=A[N-1]
        for i in range(0,N-1):
            print(s,A[i])
            s-=A[i]

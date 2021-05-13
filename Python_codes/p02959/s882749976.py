N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0

for i in range(N):
    if i%2==0:
        if A[int(i/2)]>=B[int(i/2)]:
            A[int(i/2)]-=B[int(i/2)]
            ans+=B[int(i/2)]
            B[int(i/2)]=0
        else:
            B[int(i/2)]-=A[int(i/2)]
            ans+=A[int(i/2)]
            A[int(i/2)]=0
        if A[int(i/2)+1]>=B[int(i/2)]:
            A[int(i/2)+1]-=B[int(i/2)]
            ans+=B[int(i/2)]
            B[int(i/2)]=0
        else:
            B[int(i/2)]-=A[int(i/2)+1]
            ans+=A[int(i/2)+1]
            A[int(i/2)+1]=0
    else:
        if A[N-int(i/2)]>=B[N-int(i/2)-1]:
            A[N-int(i/2)]-=B[N-int(i/2)-1]
            ans+=B[N-int(i/2)-1]
            B[N-int(i/2)-1]=0
        else:
            B[N-int(i/2)-1]-=A[N-int(i/2)]
            ans+=A[N-int(i/2)]
            A[N-int(i/2)]=0
        if A[N-int(i/2)-1]>=B[N-int(i/2)-1]:
            A[N-int(i/2)-1]-=B[N-int(i/2)-1]
            ans+=B[N-int(i/2)-1]
            B[N-int(i/2)-1]=0
        else:
            B[N-int(i/2)-1]-=A[N-int(i/2)-1]
            ans+=A[N-int(i/2)-1]
            A[N-int(i/2)-1]=0

print(ans)

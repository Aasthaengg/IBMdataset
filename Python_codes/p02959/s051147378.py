N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0

for i in range(N):
    if i%2==0:
        if A[i//2]>=B[i//2]:
            A[i//2]-=B[i//2]
            ans+=B[i//2]
            B[i//2]=0
        else:
            B[i//2]-=A[i//2]
            ans+=A[i//2]
            A[i//2]=0
        if A[i//2+1]>=B[i//2]:
            A[i//2+1]-=B[i//2]
            ans+=B[i//2]
            B[i//2]=0
        else:
            B[i//2]-=A[i//2+1]
            ans+=A[i//2+1]
            A[i//2+1]=0
    else:
        if A[N-i//2]>=B[N-i//2-1]:
            A[N-i//2]-=B[N-i//2-1]
            ans+=B[N-i//2-1]
            B[N-i//2-1]=0
        else:
            B[N-i//2-1]-=A[N-i//2]
            ans+=A[N-i//2]
            A[N-i//2]=0
        if A[N-i//2-1]>=B[N-i//2-1]:
            A[N-i//2-1]-=B[N-i//2-1]
            ans+=B[N-i//2-1]
            B[N-i//2-1]=0
        else:
            B[N-i//2-1]-=A[N-i//2-1]
            ans+=A[N-i//2-1]
            A[N-i//2-1]=0

print(ans)

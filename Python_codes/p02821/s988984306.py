import bisect
def justM(x,N):
    sum_=0
    for i in range(N):
        b=bisect.bisect_left(A,x-A[i])
        sum_+=N-b
    return sum_

N,M=map(int,input().split())
A=sorted(map(int,input().split()))
left,right=-1,(10**5)*2+1
while(right-left>1):
    mid=(right+left)//2
    s=justM(mid,N)
    if s<M:
        right=mid
    else:
        left=mid
D=left
r=[0]*(N+1)
ans=0
for i in range(N):
    r[i+1]=r[i]+A[i]
cnt=0
for i in range(N):
    b=bisect.bisect_left(A,D-A[i])
    ans+=A[i]*(N-b)+(r[N]-r[b])
    cnt+=N-b
print(ans-D*(cnt-M))
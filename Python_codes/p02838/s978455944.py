N=int(input())
A=list(map(int,input().split()))

mod=10**9+7
ans=0

for i in range(61):
    x=0
    for j in range(N):
        if A[j]>>i&0b1:
            x+=1
    now=x*(N-x)%mod
    for j in range(i):
        now=now*2%mod
    ans+=now
    ans%=mod

print(ans)
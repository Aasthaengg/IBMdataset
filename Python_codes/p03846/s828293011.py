N=int(input())
A=list(map(int,input().split()))
A.sort()
ans=1
mod=10**9+7
if N%2==0:
    for k in range(N//2):
        if A[2*k]==2*k+1 and A[2*k+1]==2*k+1:
            ans=ans*2%mod
            continue
        else:
            ans=0
            break
if N%2==1:
    if A[0]==0:
        ans=2
        for k in range(N//2-1):
            if A[2*k+2]==2*k+2 and A[2*k+1]==2*k+2:
                ans=ans*2%mod
                continue
            else:
                ans=0
                break
    else:
        ans=0
if N==1:
    if A[0]==0:
        ans=1
    else:
        ans=0
print(ans)
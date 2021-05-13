N=int(input())
A=list(map(int,input().split()))
B=[0]*3
mod=10**9+7

ans=1
for i in range(N):
    cnt=0
    idx=-1
    for j in range(3):
        if A[i]==B[j]:
            cnt+=1
            idx=j
    ans=ans*cnt
    ans=ans%mod
    B[idx]+=1
print(ans)

n,k=map(int,input().split())
mod=10**9+7
bk = [pow((k//l),n,mod) for l in range(1,k+1)]

BK=[0]*(k+1)
for i in range(k,0,-1):
    hiku=0
    for j in range(k//i+1):
        if j*i>k:
            break
        hiku+=BK[i*j]
    BK[i] = bk[i-1]-hiku

ans=0
for i,bb in enumerate(BK):
#     print(i,bb)
    ans=ans+i*bb %mod
print(ans%mod)
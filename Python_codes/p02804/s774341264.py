n,k=map(int,input().split())
A=list(map(int,input().split()))
mod=10**9+7
if k==1:
    print(0)
else:
    X=[]
    A.sort()
    x=sum(A[k-1:])
    y=sum(A[:n-k+1])
    for i in range(k,n+1):
        X.append(x-y)
        x-=A[i-1]
        y-=A[n-i]

    ans=0
    cmb=1
    for i in range(k-2,n-1):
        ans+=cmb*X[i-(k-2)]
        ans%=mod
        cmb*=(i+1)*pow(i-(k-3),mod-2,mod)
        cmb%=mod
    print(ans)
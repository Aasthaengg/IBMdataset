import copy

def f(n):
    if n==0:
        return 1
    elif n==1:
        return 2
    else:
        return f(n-1)+f(n-2)

p=10**9+7
H,W,K=map(int,input().split())

if W==1:
    ans=1
else:
    d={}
    for i in range(8):
        d[i]=f(i)
    d[-1]=d[-2]=d[-3]=1

    b=[0 for i in range(W+2)]
    a=[0 for i in range(W+2)]

    b[1]=d[W-2];b[2]=d[W-3]

    for i in range(H-1):
        for k in range(1,W+1):
            a[k]=b[k-1]*d[k-3]*d[W-k-1]
            a[k]+=b[k]*d[k-2]*d[W-k-1]
            a[k]+=b[k+1]*d[k-2]*d[W-k-2]
            a[k]%=p
        b=copy.copy(a)
    
    ans=b[K]

print(ans)
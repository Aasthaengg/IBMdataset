n,k=map(int,input().split())
v=list(map(int,input().split()))
def get(t,s): # t個のうち前からs個
    return sorted(v[:s]+v[n-(t-s):])

def f(t):
    res=0
    for i in range(t+1):
        a=get(min(t,n),min(i,n))
        tmp=sum(a)
        res=max(res,tmp)
        for j in range(min(k-t,t,n)):
            tmp-=a[j]
            res=max(res,tmp)
    return res

ans=0
for i in range(1,k+1):
    ans=max(ans,f(i))
print(ans)
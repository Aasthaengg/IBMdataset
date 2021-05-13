def power(a,n):
    x=1
    L=list(format(n,'b'))
    l=len(L)
    for i in range(l):
        if int(L[l-i-1])==1:        
            x=(x*a)%(10**9+7)
        a=(a*a)%(10**9+7)
    return x
n,k=map(int,input().split())
a=1
b=1
y=0
for i in range(n):
    a=(a*(i+1))%(10**9+7)
    b=(b*(2*n-i-1))%(10**9+7)
aa=power(a,10**9+5)
x=(b*aa)%(10**9+7)
if k<n-1:
    c=1
    d=1
    e=1
    f=1
    for i in range(k+1):
        c=(c*(n-i))%(10**9+7)
        d=(d*(i+1))%(10**9+7)
    d=power(d,10**9+5)
    c=(c*d)%(10**9+7)
    for i in range(n-k-2):
        e=(e*(n-1-i))%(10**9+7)
        f=(f*(i+1))%(10**9+7)
    f=power(f,10**9+5)
    e=(e*f)%(10**9+7)
    y=(c*e)%(10**9+7)
    if k+2<=n-1:
        for i in range(k+2,n):
            c=(c*(n-i+1))%(10**9+7)
            d=power(i,10**9+5)
            c=(c*d)%(10**9+7)
            e=(e*(n-i))%(10**9+7)
            f=power(i,10**9+5)
            e=(e*f)%(10**9+7)
            y+=(c*e)%(10**9+7)
            y=y%(10**9+7)
x=x-y
if x<0:
    x=10**9+7+x
print(x)





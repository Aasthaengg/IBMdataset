s=int(input())
p=10**9+7
if s<=2:
    print(0)
    exit()
n=s//3
ans=0
def f(n,k,p):
    if k==0:
        return 1
    elif k%2==0:
        return (f(n,k//2,p)**2)%p
    else:
        return (n*f(n,k-1,p))%p

for k in range(1,n+1):
    a=1
    b=1
    for j in range(k-1):
        a=(a*(s-3*k+1+j))%p
        b=(b*(j+1))%p
    ans=(ans+a*f(b,p-2,p))%p

print(ans%p)


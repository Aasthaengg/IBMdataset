n,m=map(int,input().split())
p=10**9+7
w=[]
M=m
i=2
cnt=0

def f(n,k,p):
    if k==0:
        return 1
    elif k%2==0:
        return (f(n,k//2,p)**2)%p
    else:
        return (n*f(n,k-1,p))%p

while i*i<=M:
    if m%i==0:
        cnt+=1
        m=m//i
    else:
        if cnt>=1:
            w.append(cnt)
        cnt=0
        i+=1
if m>1:
    w.append(1)

ans=1
for x in w:
    a=1
    for i in range(x):
        a=(a*(n+i))%p
    b=1
    for i in range(x):
        b=(b*(i+1))%p

    ans=(ans*a*f(b,p-2,p))%p
print(ans%p)


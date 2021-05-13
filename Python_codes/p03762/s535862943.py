mod=10**9+7
def f(a):
    c=0
    for i in range(len(a)):
        c+=a[i]-a[0]
    d=c
    for i in range(1,len(a)-1):
        d+=c-(len(a)-i)*(a[i]-a[i-1])
        c-=(len(a)-i)*(a[i]-a[i-1])
    return d%mod
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(f(a)*f(b)%mod)
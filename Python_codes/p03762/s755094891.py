def modpow(a,n,p):
    if n==0:
        return 1
    x=modpow(a,n//2,p)
    x=(x*x)%p
    if (n%2)==1:
        x=(x*a)%p
    return x%p
def modinv(a,p):
    return modpow(a,p-2,p)
n,m=map(int,input().split())
h=list(map(int,input().split()))
w=list(map(int,input().split()))
tate=0
yoko=0
p=10**9+7
for i in range(n-1):
    weight=((i+1)*(n-1-i))%p
    tate=(tate+weight*((h[i+1]-h[i])%p))%p
for i in range(m-1):
    weight=((i+1)*(m-1-i))%p
    yoko=(yoko+weight*((w[i+1]-w[i])%p))%p
print((tate*yoko)%p)

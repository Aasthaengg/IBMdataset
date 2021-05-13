import collections
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
N,M=map(int,input().split())
l=[]
pf={}
m=M
p=10**9+7
frac=[1]*(2*(10**7))
ans=1
for i in range(2,int(m**0.5)+1):
    while m%i==0:
        pf[i]=pf.get(i,0)+1
        m//=i
if m>1:pf[m]=1
#print(pf)
for i in range(1,2*(10**7)):
    frac[i]=(frac[i-1]*i)%p
#print(frac[:7])
keys=list(pf.keys())
values=list(pf.values())
for i in range(len(keys)):
    l.append([keys[i],values[i]])
#print(l)
for i in range(len(l)):
    a=l[i][1]
    ans=(ans*frac[a+N-1]*modinv(frac[a],p)*modinv(frac[N-1],p))%p
print(ans%p)
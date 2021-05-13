from collections import Counter

n,m=map(int,input().split())
primes=[]

mod=10**9+7

def modinv(x):
    return pow(x,mod-2,mod)


i=2
while i*i<=m:
    if m%i==0:
        while m%i==0:
            primes.append(i)
            m//=i
    
    i+=1
if m>1:
    primes.append(m)

cnt=Counter(primes)

invlst=[1]*(2*10**5)
factlst=[1]*(2*10**5)

for i in range(2,2*10**5):
    invlst[i]=modinv(i)*invlst[i-1]
    factlst[i]=i*factlst[i-1]
    invlst[i]%=mod
    factlst[i]%=mod
ans=1
for v in cnt.values():
    ans*=factlst[v+n-1]*invlst[n-1]*invlst[v]
    ans%=mod

print(ans)

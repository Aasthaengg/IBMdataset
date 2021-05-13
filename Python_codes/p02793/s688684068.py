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
from fractions import gcd
N=int(input())
A=list(map(int,input().split()))
new=[0]*N
A.sort()
insuu=[0]*(A[N-1]+1)
pf={}
l=[]
ans=1
cnt=0
p=(10**9)+7

for i in range(N):
    m = A[i]
    for j in range(2,int(m**0.5)+1):
        while m%j==0:
            pf[j]=pf.get(j,0)+1
            m//=j
    if m>1:pf[m]=1
    #print(pf)
    keys=list(pf.keys())
    values=list(pf.values())
    pf={}
    for j in range(len(keys)):
        if insuu[keys[j]]<values[j]:
            insuu[keys[j]]=values[j]
        #print(insuu)
    #print(l)
for i in range(1,A[N-1]+1,1):
    if insuu[i]>0:
        ans=ans*pow(i,insuu[i])
#print(ans)
for i in range(N):
    #print((ans*modinv(A[i],p))%p)
    cnt=(cnt+(ans*modinv(A[i],p))%p)%p
print(cnt%p)


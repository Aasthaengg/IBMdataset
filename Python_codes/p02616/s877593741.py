n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort(key=lambda x: -abs(x))
mod=10**9+7
p=1
mm=0
for i in range(k):
    if a[i]<0:
        mm+=1
    p*=a[i]
    p%=mod
if n==k or mm%2==0:
    print(p)
    exit()
    
m=0
for i in a:
    if i<=0:
        m+=1
if m==n:
    p=1
    for i in range(k):
        p*=a[n-i-1]
        p%=mod
    print(p)
    exit()
b1=[]
b2=[]
for i in range(k):
    if len(b1)==0 and a[k-1-i]>=0:
        b1.append(a[k-1-i])
    if len(b2)==0 and a[k-1-i]<0:
        b2.append(a[k-1-i])
for i in range(n-k):
    if len(b1)==1 and a[k+i]<0:
        b1.append(a[k+i])
    if len(b2)==1 and a[k+i]>=0:
        b2.append(a[k+i])
f=0
if len(b1)==len(b2)==2:
    if b1[1]*b2[0]>=b1[0]*b2[1]:
        f=1
    else:
        f=2
elif len(b2)<2:
    f=1
else:
    f=2

if f==1:
    p*=b1[1]*pow(b1[0],mod-2,mod)
    print(p%mod)
    exit()
else:
    p*=b2[1]*pow(b2[0],mod-2,mod)
    print(p%mod)
    exit()

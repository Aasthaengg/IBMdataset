from collections import defaultdict
n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=pow(10,9)+7
a0=0
d=defaultdict(lambda:0)
for i in range(n):
    a0+=len([s for s in a[:i] if s>a[i]])
    d[a[i]]+=1
keys=sorted(d.keys())
matagi=0
ni=n
for ky in keys:
    c=d[ky]
    ni-=c
    matagi+=ni*c
ans=(k*a0)%mod
ans+=(matagi*(k*(k-1))//2)%mod
print(ans%mod)
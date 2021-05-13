import numpy as np

n=10**6
nsq=10**3
mod=10**9+7
fact=np.arange(n,dtype=np.int64).reshape(nsq,nsq); fact[0,0]=1
for n in range(1,nsq):
    fact[:,n]*=fact[:,n-1]; fact[:,n]%=mod
for n in range(1,nsq):
    fact[n]*=fact[n-1,-1];fact[n]%=mod
fact=fact.ravel()

n,m=map(int,input().split())
p=fact[n]
q=fact[m]
if abs(n-m)>=2:
    print(0)
elif abs(n-m)==1:
    print((p*q)%(10**9+7))
else:
    print(2*(p*q)%(10**9+7))

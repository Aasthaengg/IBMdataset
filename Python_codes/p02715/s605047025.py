n,k=map(int,input().split())
dlist=[[]for i in range(k+1)]
mod = 10**9+7
num=[0]*(k+1)
idx=0
for i in range(1,k+1):
    num[i]=pow(k//i,n,mod)
    for p in range(i*2,k+1,i):
        dlist[p].append(i)
for i in range(k,0,-1):
    for d in dlist[i]:
        num[d]=(num[d]-num[i])%mod
print(sum([i*x for i,x in enumerate(num)])%mod)
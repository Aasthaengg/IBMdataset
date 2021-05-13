n,k=map(int,input().split())
mod=998244353
lr=[]
for i in range(k):
    lr.append(list(map(int,input().split())))
d=[0]*(n+1)
d[0]=1
for i in range(n): 
    for l,r in lr:
        r+=1
        d[min(n,i+l)]+=d[i]
        d[min(n,i+r)]-=d[i]
    if i!=0:
        d[i+1]+=d[i]
    d[i+1]%=mod
#print(d)
print(d[n-1]%mod)

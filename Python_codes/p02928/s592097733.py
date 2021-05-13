n,k=map(int,input().split())
a=list(map(int,input().split()))
d={}
key=[]
n_in=0
n_out=0
ans=0
#k%=(10**9+7)
for i in range(n):
    try:
        d[a[i]]+=1
    except:
        d[a[i]]=1
        key.append(a[i])
        key.sort()
    ind=key.index(a[i])
    for j in range(ind+1,len(key)):
        n_in+=d[key[j]]
for val in a:
    ind=key.index(val)
    for j in range(ind+1,len(key)):
        n_out+=d[key[j]]

ans+=n_in*k
ans+=n_out*(k-1)*k//2
ans%=10**9+7
print(ans)

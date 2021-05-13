mod=998244353
w=[]
dp=[0]*200005
ds=[0]*200005
dp[1]=1
ds[1]=1
n,k=map(int,input().split())
for i in range(k):
    a,b=map(int,input().split())
    w.append((a,b))

for i in range(2,n+1):
    for j,k in w:
        li=i-k
        ri=i-j
        if ri<0: continue
        li=max(li,1)
        dp[i]+=ds[ri]-ds[li-1];
        dp[i]%=mod
    ds[i]=ds[i-1]+dp[i]
    ds[i]%=mod

print(dp[n])

n,m=map(int,input().split()) #<=2*10**3
#n
s=list(map(int,input().split()))
#m
t=list(map(int,input().split()))
mod=10**9+7
ans=[0]*m

for u in s:
    h=[0]*m
    if u==t[0]:
        h[0]=1
    for i in range(1,m):
        if t[i]==u:
            h[i]+=ans[i-1]+1
        h[i]+=h[i-1]
    for i in range(m):
        ans[i]=(ans[i]+h[i])%mod
print((ans[-1]+1)%mod)
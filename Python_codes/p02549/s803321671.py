n,k=map(int,input().split())
dp=[0 for i in range(n+1)]
dp[1]=1
accum=[0 for i in range(n+1)]
accum[1]=1
s=[]
for i in range(k):
    x,y=map(int,input().split())
    s.append([x,y])
for i in range(2,n+1):
    for j in s:
        l,r=j
        tmpl=i-r
        tmpr=i-l
        if(tmpl<1):
            tmpl=1
        if(tmpr>=i):
            tmpr=i-1
        if(tmpr<0):
            continue
        dp[i]+=accum[tmpr]-accum[tmpl-1]
        dp[i]%=998244353
    accum[i]=dp[i]+accum[i-1]
    accum[i]%=998244353
print(dp[n]%998244353)
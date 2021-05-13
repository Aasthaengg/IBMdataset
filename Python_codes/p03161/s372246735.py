n,k=map(int,input().split())
l=[int(x) for x in input().split()]
dp=[0]*n
dp[0]=0
for i in range(1,n):
    m=10**20
    if i-k<=0:
        for j in range(i):
            t=dp[j]+abs(l[i]-l[j])
            m=min(t,m)
    else:
        for j in range(i-1,i-k-1,-1):
            t=dp[j]+abs(l[i]-l[j])
            m=min(t,m)
    dp[i]=m
print(dp[n-1])
h,n=map(int,input().split())
dp=[10000000000]*(10**5+1)
dp[0]=0

a=[]
b=[]
for _ in range(n):
    a1,b1=map(int,input().split())
    a.append(a1)
    b.append(b1)
for i in range(10**4+2):
    
    for j in range(n):
        dp[i+a[j]]=min((dp[i+a[j]]),dp[i]+b[j])
print(min(dp[h:]))
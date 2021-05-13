n,k=map(int,input().split())
l=list(map(int,input().split()))
dp=[0]*n
for i in range(1,n):    
    start=max(0,i-k)
    dp[i]=min(dp[j]+abs(l[i]-l[j]) for j in range(start,i))
print(dp[-1])
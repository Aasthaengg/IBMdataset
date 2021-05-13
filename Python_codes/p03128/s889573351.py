n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
nums=[0,2,5,5,4,5,6,3,7,6]
dp=[-1]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for x in a:
        if i-nums[x]>=0:
            dp[i]=max(dp[i-nums[x]]+1,dp[i])
k=dp[n]
ans=[]
for i in range(k):
    for x in a:
        if n-nums[x]<0:
            continue
        if dp[n-nums[x]]==dp[n]-1:
            n-=nums[x]
            ans.append(x)
            break
print("".join(list(map(str,ans))))

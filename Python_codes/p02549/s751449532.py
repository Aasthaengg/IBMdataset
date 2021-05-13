p=998244353
n,k=map(int,input().split())
kukan=[]
for i in range(k):
    l,r=map(int,input().split())
    kukan.append((l,r))
dp=[0]*n
sdp=[0]*(n+1)
dp[0]=1
sdp[1]=1
for i in range(1,n):
    for l,r in kukan:
        left=max(0,i-r)
        right=max(0,i-l+1)
        dp[i]=(dp[i]+sdp[right]-sdp[left])%p
    sdp[i+1]=(sdp[i]+dp[i])%p
print(dp[-1])
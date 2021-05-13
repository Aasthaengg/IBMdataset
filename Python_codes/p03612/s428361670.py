n = int(input())
p_input = list(map(int,input().split()))

dp=[0]*n
if p_input[0]==1:
    dp[0]=1
for i in range(1,n):
    if p_input[i]==i+1:
        dp[i]=dp[i-1]+1
        dp[i-1]=0
ans=0
for i in range(n):
    if dp[i]%2==0:
        ans+=dp[i]//2
    else:
        ans+=dp[i]//2+1
print(ans)
#reversi
n=int(input())
lists=[]
for i in range(n):
    a=int(input())
    lists.append(a)
dp=[0 for i in range(n+1)]
dp[0]=1
mod=10**9+7
before=[0 for i in range(2*10**5+1)]

for i in range(n):
    a=lists[i]
    if before[a]==0:
        dp[i+1]=dp[i]
        before[a]=i+1
        continue
        
    elif before[a]!=0:
        if before[a]==i:
            before[a]=i+1
            dp[i+1]=dp[i]
        else:
            dp[i+1]=(dp[i]+dp[before[a]])%mod

            before[a]=i+1
print(dp[n]%mod)  

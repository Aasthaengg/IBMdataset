sixexp=[6**i for i in range(1,7)]
nineexp=[9**i for i in range(1,6)]
lis=[1]+sixexp+nineexp

n=int(input())

dp=[1000000 for i in range (n+1)]
dp[0]=0

for i in range(1,n+1):
    for j in lis:
        if i-j>=0:
            dp[i]=min(dp[i],dp[i-j]+1)

print(dp[n])
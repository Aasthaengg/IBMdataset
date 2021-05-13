n=int(input())
l=[int(i) for i in input().split()]
dp=[-1]*(n)
dp[0]=0
dp[1]=abs(l[1]-l[0])
for i in range(2,n):
    dp[i]=min(dp[i-1]+abs(l[i]-l[i-1]),dp[i-2]+abs(l[i-2]-l[i]))
            
print(dp[-1])

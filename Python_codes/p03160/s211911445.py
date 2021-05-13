n=int(input())
l=[int(x) for x in input().split()]
dp=[0]*n
for i in range(n):
    if i==0:
        dp[i]=0
    elif i==1:
        dp[i]=abs(l[i]-l[i-1])
    else:
	    dp[i]=min(dp[i-1]+abs(l[i]-l[i-1]),dp[i-2]+abs(l[i]-l[i-2]))
print(dp[n-1])

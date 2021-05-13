n=int(input())
c=list(int(input()) for i in range(n))
dp=[0]*n
rec=[0]*(2*10**5+1)
dp[0]=1
rec[c[0]]=1
for i in range(1,n):
	if c[i]==c[i-1]:
		dp[i]=dp[i-1]
		continue
	dp[i]=(dp[i-1]+rec[c[i]])%(10**9+7)
	rec[c[i]]=dp[i]
print(dp[-1])
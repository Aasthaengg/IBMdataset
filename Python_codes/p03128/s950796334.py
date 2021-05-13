n,_,*a=map(int,open(0).read().split())
ref={1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
dp=[0]+[-float('inf')]*(n+9)
for i in range(n+1):
	for x in a:
		if dp[i]<dp[i-ref[x]]*10+x:
			dp[i]=dp[i-ref[x]]*10+x
print(dp[n])
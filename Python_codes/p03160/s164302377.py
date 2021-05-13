def solve(arr,n):
	dp=[0]*n 
	if n==2:
		print(abs(arr[0]-arr[-1]))
		return 
	dp[0]=0 
	dp[1]=abs(arr[0]-arr[1]) 
	for i in range(2,n):
		dp[i]=min(dp[i-1]+abs(arr[i-1]-arr[i]),dp[i-2]+abs(arr[i-2]-arr[i])) 
	print(dp[-1]) 
n=int(input())
a=[int(x) for x in input().split()] 
solve(a,n) 
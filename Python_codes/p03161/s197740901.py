def solve(arr,n,k):
	if k==1:
		ss=0 
		for i in range(1,n):
			ss+=abs(arr[i]-arr[i-1]) 
		print(ss) 
		return  
	if k>=n:
		print(abs(arr[-1]-arr[0]))
		return
	dp=[0]*n 
	for i in range(k):
		dp[i]=abs(arr[i]-arr[0])  
	for i in range(k,n):
		f=float('inf') 
		for x in range(1,k+1):
			f=min(dp[i-x]+abs(arr[i-x]-arr[i]),f)  
		dp[i]=f 
	#print(dp)
	print(dp[-1]) 
n,k=map(int,input().split()) 
a=[int(x) for x in input().split()] 
solve(a,n,k) 
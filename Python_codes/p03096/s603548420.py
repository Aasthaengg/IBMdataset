mod=(10**9)+7
a=[0]*200005
dp=[0]*200005
s=[0]*200005
cnt=0

n=int(input())+1
for i in range (1, n):
	x=int(input())
	if x!=a[cnt]:
		cnt=cnt+1
		a[cnt]=x

cnt+=1

dp[0]=1
for i in range (1, cnt):
	dp[i]=dp[i-1]
	dp[i]=(dp[i]+s[a[i]])%mod
	s[a[i]]=(s[a[i]]+dp[i-1])%mod

print(dp[cnt-1])
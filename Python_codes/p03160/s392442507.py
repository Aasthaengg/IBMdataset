import sys
sys. setrecursionlimit(100009)
n=int(input())
hr=list(map(int,input().split()))
dp=[-1]*(n+1)
def cost(i):
	if i>=n-1:
		return 0
	if dp[i]!=-1:
		return dp[i]
	if i<n-2:
		a=abs(hr[i]-hr[i+2])+cost(i+2)
	b=abs(hr[i]-hr[i+1])+cost(i+1)
	if i>=n-2:
		a=b
	x=min(a,b)
	dp[i]=x
	return x
print(cost(0))
import sys
input=sys.stdin.readline
#for _ in range(int(input())):
#	n=int(input())
n,k=map(int,input().split())
#	s=input().strip()
a=list(map(int,input().split()))
dp=[False]*(k+1)
for i in range(1,k+1):
	for j in range(n):
		if i-a[j]>=0 and dp[i-a[j]]==False:
			dp[i]=True;break
if dp[-1]:print("First")
else:print("Second")
import sys
input=sys.stdin.readline
#for _ in range(int(input())):
#	n=int(input())
#	n,m=map(int,input().split())
#	s=input().strip()
sys.setrecursionlimit(10**9)
def dfs(i):
	if dp[i]!=-1:return dp[i]
	c=0
	for j in v[i]:c=max(c,dfs(j)+1)
	dp[i]=c
	return c

n,m=map(int,input().split())
v=[[] for i in range(n+1)]
for i in range(m):
	x,y=map(int,input().split())
	v[x].append(y)
dp = [-1]*(n+1) 
m=0
for i in range(1,n+1):
	m=max(m,dfs(i))
print(m)
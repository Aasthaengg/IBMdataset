import sys
sys.setrecursionlimit(10**5*5)
n=int(input())
ab=[[]for _ in range(n)]
for _ in range(n-1):
	a,b=map(int,input().split())
	ab[a-1].append(b-1)
	ab[b-1].append(a-1)
c=list(map(int,input().split()))
c.sort()
print(sum(c)-c[-1])
ans=[-1]*n
cnt=0
node=[]
visited=[0]*n
ans=[-1]*n
def dfs(x):
	global cnt
	ans[x]=c[-cnt-1]
	visited[x]=1
	for next in ab[x]:
		if visited[next]==0:
			cnt+=1
			dfs(next)
dfs(0)
print(*ans)


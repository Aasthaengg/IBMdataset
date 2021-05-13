inf=10**10
n,m=map(int,input().split())
x=[inf]*n
con=[[] for _ in range(n)]
for i in range(m):
	l,r,d=map(int,input().split())
	con[l-1].append((r-1,d))
	con[r-1].append((l-1,-d))
from collections import deque
for i in range(n):
	if x[i]==inf:
		x[i]=0
		q=deque([i])
		while q:
			e=q.pop()
			for j,k in con[e]:
				if x[j]==inf:
					q.append(j)
					x[j]=x[e]+k
				elif x[j]!=x[e]+k:
					print("No")
					exit()
print("Yes")
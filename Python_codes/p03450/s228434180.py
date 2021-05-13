n,m=map(int,input().split())
ans=[10**10]*n
edge=[[]for _ in range(n)]
for _ in range(m):
	l,r,d=map(int,input().split())
	l-=1
	r-=1
	edge[l].append([r,d])
	edge[r].append([l,-d])
for i in range(n):
	if ans[i]==10**10:
		ans[i]=0
		Q=[i]
		while Q:
			P=[]
			for i in Q:
				for j,d in edge[i]:
					if ans[j]==10**10:
						P+=[j]
						ans[j]=ans[i]+d
			Q=P
for i in range(n):
	for j,k in edge[i]:
		if ans[i]+k!=ans[j]:print("No");exit()
print("Yes")
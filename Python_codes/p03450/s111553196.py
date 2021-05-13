n,m=map(int,input().split())
x=[[]for _ in range(n+1)]
y=[None]*(n+1)
a="Yes"
for num in range(m):
	i,j,k=map(int,input().split())
	x[i].append((j,k))
	x[j].append((i,-k))
for i in range(1,n+1):
	if y[i]==None:
		y[i]=0;q=[i]
		while q:
			p=q.pop()
			for j,k in x[p]:
				if y[j]==None:q+=[j];y[j]=y[p]+k
for i in range(1,n+1):
	for j,k in x[i]:
		if y[i]+k!=y[j]:a="No"
print(a)
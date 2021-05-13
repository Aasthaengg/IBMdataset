n,m=map(int,input().split())
g=[[] for i in range(n)]
for i in range(m):
	u,v=map(int,input().split())
	u-=1
	v-=1
	g[u].append(v)
	g[v].append(u)

vis=[False]*n
stk=[]

cnt=0
tt=0
for i in range(n):
	if not vis[i]:
		cnt+=1
		stk.append(i)
	while len(stk)!=0:
		u=stk[-1]
		stk.pop()
		if vis[u]:
			continue
		vis[u]=True
		for v in g[u]:
			tt+=1
			if not vis[v]:
				stk.append(v)
print(cnt-1)

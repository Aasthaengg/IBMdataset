N,M=[int(x) for x in input().split()]
INF=1000000000000000
adj=[[INF for i in range(N+1)] for j in range(N+1)]

for i in range(N+1):
	adj[i][i]=0
	
A=[]
B=[]
C=[]
ans=M

for i in range(M):
	a,b,c=[int(x) for x in input().split()]
	adj[a][b]=min(adj[a][b],c)
	adj[b][a]=min(adj[b][a],c)
	A.append(a)
	B.append(b)
	C.append(c)

for k in range(1,N+1):
		for i in range(1,N+1):
			for j in range(1,N+1):
				adj[i][j]=min(adj[i][k]+adj[k][j],adj[i][j])


for i in range(M):
	temp=1
	for j in range(1,N+1):
		if adj[j][A[i]]+C[i]==adj[j][B[i]]:
			temp=0
	if temp==0:
		ans-=1
print(ans)
		





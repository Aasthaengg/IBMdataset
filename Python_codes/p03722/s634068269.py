N,M=[int(x) for x in input().split()]
A=[]
B=[]
C=[]

for i in range(M):
	a,b,c=[int(x) for x in input().split()]
	A.append(a-1)
	B.append(b-1)
	C.append(-c)
INF=10000000000000
dist=[INF for i in range(N)]

dist[0]=0


for temp in range(N-1):
	for i in range(M):
		if dist[A[i]]!=INF:
			if dist[B[i]]>dist[A[i]]+C[i]:
				dist[B[i]]=dist[A[i]]+C[i]

checker=[0 for i in range(N)]
ans=dist[N-1]

for temp in range(N):
	for i in range(M):
		if dist[A[i]]!=INF:
			if dist[B[i]]>dist[A[i]]+C[i]:
				dist[B[i]]=dist[A[i]]+C[i]
				checker[B[i]]=1
			if checker[A[i]]==1:
				checker[B[i]]=1

if checker[N-1]==1:
	print("inf")
else:
	print(-ans)

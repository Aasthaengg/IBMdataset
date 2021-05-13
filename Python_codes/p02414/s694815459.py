n,m,l=list(map(int,input().split()))
A=[]
B=[]
for i in range(n):
	A.append(list(map(int,input().split())))
for i in range(m):
	B.append(list(map(int,input().split())))

res=[[0 for i in range(l)] for i in range(n)]

for i in range(n):
	for k in range(l):
		for j in range(m):
			res[i][k]+=A[i][j]*B[j][k]

for i in res:
	print(" ".join(list(map(str,i))))
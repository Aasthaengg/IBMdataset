n,m=list(map(int,input().split()))
mat=[]
for i in range(n):
	mat.append(list(map(int,input().split())))

vec=[]
for i in range(m):
	vec.append(int(input()))

res=[]
for i in range(n):
	c=0
	for j in range(m):
		c+=mat[i][j]*vec[j]
	res.append(c)
for i in res:
	print(i)
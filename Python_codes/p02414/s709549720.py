n,m,l=map(int,raw_input().split())
a=[]
b=[]
c=[[0 for k in range(l)] for i in range(n)]

for i in range(n):
	a.append(map(int,raw_input().split()))
for j in range(m):
	b.append(map(int,raw_input().split()))

for i in range(n):
	for k in range(l):
		for j in range(m):
			c[i][k] += a[i][j]*b[j][k]
for i in range(n):
	print ' '.join(map(str,c[i]))
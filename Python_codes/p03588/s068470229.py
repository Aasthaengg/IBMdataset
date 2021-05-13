n=int(input())
d={}
m=0
for i in range(n):
	a,b=map(int,input().split())
	d[a]=b
	m=max(m,a)
print(m+d[m])
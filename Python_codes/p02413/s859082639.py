r,c=list(map(int,input().split()))
l=[]
for i in range(r):
	a=list(map(int,input().split()))
	a.append(sum(a))
	l.append(a)
b=[]
for i in range(c+1):
	c=0
	for j in range(r):
		c+=l[j][i]
	b.append(c)
l.append(b)

for i in l:
	print(" ".join(list(map(str,i))))
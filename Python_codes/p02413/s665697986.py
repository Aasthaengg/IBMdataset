n=list(map(int,input().split()))
x=[]
b=[]
s=[]
for i in range(n[0]):
	x.append(list(map(int,input().split())))

for i in range(n[0]):
	a=0
	for j in range(n[1]):
		a+=x[i][j]
	x[i].append(a)
	print(' '.join(list(map(str,x[i]))))
for i in range(n[1]+1):
	l=0
	for j in range(n[0]):
		l+=x[j][i]
	s.append(l)
print(' '.join(list(map(str,s))))
	


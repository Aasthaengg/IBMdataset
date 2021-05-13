a,b=list(map(int,input().split()))
c = [0] * a
for i in range(b):
	x,y=list(map(int,input().split()))
	c[x-1]=c[x-1]+1
	c[y-1]=c[y-1]+1

for j in range(a):
	print(c[j])
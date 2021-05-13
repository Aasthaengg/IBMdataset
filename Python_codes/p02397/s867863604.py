L1= []
L2= []
N= 0
while True:
	x,y= map(int,input().split())
	if(x==y==0):
		break
	if(x> y):
		x,y= y,x
	L1.append(x)
	L2.append(y)
	N= N+1

for i in range(N):
	print(L1[i],L2[i])
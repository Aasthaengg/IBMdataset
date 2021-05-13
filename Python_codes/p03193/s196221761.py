n,h,w=map(int,input().split(" "))
c=0
for i in range(0,n):
	a,b=map(int,input().split(" "))
	if(a>=h and b>=w):
		c=c+1
print(c)
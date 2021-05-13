a,b=map(int,input().split())
if b==1: print(0)
elif a>=b: print(1)
else:
	x=a+a-1
	t=1
	while x<b:
		t+=1
		x+=a-1
		pass
	print(t+1)
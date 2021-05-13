a,b=map(int,input().split())
c=int(str(a)+str(b))

if c==int(c**(1/2))**2:
	print("Yes")
else:
	print("No")
a,b,c,d,r=map(int,input().split())

if a>0:
	if c<0:
		print("No")
		exit()

if a<0:
	if c>0:
		print("No")
		exit()		

if b>0:
	if d<0:
		print("No")
		exit()

if b>0:
	if d<0:
		print("No")
		exit()

a=abs(a)
b=abs(b)
c=abs(c)
d=abs(d)

a-=r*2
b-=r*2
c-=r
d-=r

if 0<=c and 0<=d and 0<=a and 0<=b and c<=a and d<=b:
	print("Yes")
else:
	print("No")
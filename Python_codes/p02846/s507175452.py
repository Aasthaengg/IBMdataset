from math import ceil
t1,t2,a1,a2,b1,b2=map(int,open(0).read().split())
w,x,y,z=t1*a1,t2*a2,t1*b1,t2*b2
if w+x==y+z:
	print("infinity")
	exit()
if (w-y)*(w+x-y-z)>0:
	print(0)
	exit()
a1=min(w,y)
b1=max(w,y)
c1=max(w+x,y+z)
c2=min(w+x,y+z)
print(2*int((b1-a1)//(c1-c2))+int((b1-a1)%(c1-c2)>0))
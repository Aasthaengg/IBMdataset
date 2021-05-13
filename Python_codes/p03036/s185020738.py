def task():
	a=input().split()
	r=int(a[0])
	d=int(a[1])
	x=int(a[2])
	for i in range (10):
		print((r*x)-d)
		x=(r*x-d)
		
t=1
while(t>0):
		task()
		t-=1

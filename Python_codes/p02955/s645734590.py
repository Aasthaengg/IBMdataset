n,k,*l=map(int,open(0).read().split())
def f(n):
	d=[]
	for i in range(1,int(n**0.5)+1):
		if n%i== 0:
			d+=[i]
			if i!=n//i:
				d+=[n//i]
	d.sort()
	return d[::-1]
for d in f(sum(l)):
	a=sorted([m%d for m in l])
	if sum(a[:n-sum(a)//d])<=k:
		print(d);exit()

n,*l=map(int,open(0).read().split())
sum_n=sum(l)
for i in range(n):
	if 2*l[i]>=sum_n:
		print('No')
		import sys
		sys.exit()
print('Yes')
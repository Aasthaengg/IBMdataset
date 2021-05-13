n,m,d=map(int,raw_input().split())

if n <= 2*d or d == 0:
	print float(m-1)/n
else:
	print (m-1)*float(2*n-2*d)/(n*n)
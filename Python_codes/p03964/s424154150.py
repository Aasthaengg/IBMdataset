a,b = 1,1
for i in range(int(raw_input())):
	n,d = map(int, raw_input().split())
	q = max((a+n-1)/n, (b+d-1)/d)
	a,b= n*q, d*q
print a+b
for i in range(int(raw_input())):
	n,d = map(int, raw_input().split())
	if i == 0:
		a,b = n,d
	else:
		q = max((a+n-1)/n, (b+d-1)/d)
		a = n*q
		b = d*q



print a+b
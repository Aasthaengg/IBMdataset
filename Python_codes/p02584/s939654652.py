result = 2e50
X, K, D = map(int, input().split())

if (X < 0):
	lo, hi = 0, K
	while (lo < hi):
		mid = int(lo+ (hi - lo) / 2)
		if (X + mid*D >= 0):
			hi = mid;
		else:
			lo = mid + 1;
	if (X + hi*D < 0):
		p1 = hi
		if (abs(X + p1*D) < result):
			result = abs(X + p1*D)
	else:
		p1 = lo
		rem1 = K - p1
		if (rem1%2 == 1):
			result = min((result, abs(X + p1*D + D), abs(X + p1*D - D)))
		p2 = lo - 1
		rem2 = K - p2
		if (rem2%2 == 1):
			result = min((result, abs(X + p2*D + D), abs(X + p2*D - D)))
	print(result)
elif (X > 0):
	lo, hi = 0, K
	while (lo < hi):
		mid = int(lo+ (hi - lo) / 2)
		if (X - mid*D <= 0):
			hi = mid;
		else:
			lo = mid + 1
	if (X - hi*D > 0):
		p1 = hi;
		if (abs(X - p1*D) < result):
			result = abs(X - p1*D)
	else:
		p1 = lo
		rem1 = K - p1
		if (rem1%2 == 1):
			result = min((result, abs(X - p1*D - D), abs(X - p1*D + D)))
		p2 = lo - 1;
		rem2 = K - p2
		if (rem2%2 == 1):
			result = min((result, abs(X - p2*D - D), abs(X - p2*D + D)))
	print(result)
else:
	if (K%2 == 1):
		print(D)
	else:
		print(0)

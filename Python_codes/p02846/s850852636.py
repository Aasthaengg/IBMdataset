t1, t2 = map(int, raw_input().split(' '))
a1, a2 = map(int, raw_input().split(' '))
b1, b2 = map(int, raw_input().split(' '))
v1 = a1 * t1 + a2 * t2
v2 = b1 * t1 + b2 * t2
if v1 == v2:
	print('infinity')
else:
	if(v1 < v2):
		v1, v2 = v2, v1
		a1, a2, b1, b2 = b1, b2, a1, a2
	lo = 0
	hi = 10**100
	ans = 0
	while lo <= hi:
		mid = (lo + hi) / 2
		at_a = mid * v1
		at_b = mid * v2
		if at_b + b1 * t1 >= at_a + a1 * t1:
			ans = mid
			lo = mid + 1
		else:
			hi = mid - 1
	mv = 0
	if ans * v1 + a1 * t1 < ans * v2 + b1 * t1:
		mv = 1
	print(2*ans + mv)

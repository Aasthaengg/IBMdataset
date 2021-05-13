def f():
	from math import ceil
	T1,T2 = map(int,input().split())
	A1,A2 = map(int,input().split())
	B1,B2 = map(int,input().split())
	if B1 > A1:
		A1,A2,B1,B2 = B1,B2,A1,A2
	diff1 = (A1 - B1) * T1
	fac = (B2 - A2) * T2 - diff1
	if fac == 0:
		print("infinity")
	elif diff1 / fac < 0:
		print(0)
	elif diff1 / fac <= 1:
		print(1)
	else:
		print(2 * ceil(diff1 / fac) - int(diff1 % fac != 0))
f()
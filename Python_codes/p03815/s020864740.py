x = int(input())
if x <= 6:
	print(1)
else:
	A = x//11
	if x%11 == 0:
		print(2*A)
	else:
		B = x%11
		if B <= 6:
			print(2*A+1)
		else:print(2*A+2)
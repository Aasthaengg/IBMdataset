n, a, b = map(int, input().split())
if n == 1:
	if a != b:
		print (0)
	else:
		print (1)
elif a > b:
	print (0)
else:
	mn = a + b + (n-2)*a
	mx = a + b + (n-2)*b
	print (mx-mn+1)
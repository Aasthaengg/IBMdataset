n, a, b = map(int, input().split())
if n == 1:
	if a != b:
		print (0)
	else:
		print (1)
else:
	print (max((n-2)*(b-a)+1,0))
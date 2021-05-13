s = input()
n = len(s)
if n == 1:
	print(s)
elif n == 2:
	print(9)
elif n == 3:
	print(9+(int(s)-99))
elif n == 4:
	print(9+900)
elif n == 5:
	print(9+900+(int(s)-9999))
else:
	print(90909)

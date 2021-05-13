s = input()
n = len(s)
if (n == 3):
	for i in range(n):
		print(s[n-i-1],end = "")
	print()
else:
	print(s)
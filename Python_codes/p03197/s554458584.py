n = int(input())
a = [int(input()) for i in range(n)]

if any (a[i] % 2 == 1 for i in range(n)):
	print("first")
else:
	print("second")
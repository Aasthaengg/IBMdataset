n, k = map(int, input().split())
if n<6:
	print("0")
elif n < 13:
	print(k//2)
else:
	print(k)
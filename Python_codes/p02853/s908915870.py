x, y = map(int, input().split())
a = [300000, 200000, 100000]

if x > 3 and y > 3:
	print(0)
elif x == 1 and y == 1:
	print(1000000)
elif x <= 3 and y <= 3:
	print(a[x-1] + a[y-1])
elif x <= 3 and y > 3:
	print(a[x-1])
elif y <= 3 and x > 3:
	print(a[y-1])
x = int(input())
for i in range(1000):
	if 100*i <= x <= 105*i:
		print(1)
		break
else:
	print(0)
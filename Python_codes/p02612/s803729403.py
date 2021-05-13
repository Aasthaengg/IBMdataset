n = int(input())
num = int(n / 1000)

if(n % 1000 == 0):
	print(0)
else:
	num += 1
	print(num * 1000 - n)

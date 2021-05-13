def SoN(x):
	ans = 0
	while 1:
		if x<10:
			ans += x
			return ans
		else:
			ans += x % 10
			x //= 10

while 1:
	x = int(input())
	if x==0:
		break
	print(SoN(x))

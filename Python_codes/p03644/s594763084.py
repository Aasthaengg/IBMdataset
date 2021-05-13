n = int(input())
result = 0
if n == 1:
	print(1)
else:
	while(True):
		if 2 ** result == n:
			break
		if 2 ** result > n:
			result -= 1
			break
		result += 1
	print(2 ** result)
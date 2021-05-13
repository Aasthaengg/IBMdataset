n = int(input())
result = 0
while(True):
	if 2 ** result == n:
		break
	if 2 ** result > n:
		result -= 1
		break
	result += 1
print(2 ** result)
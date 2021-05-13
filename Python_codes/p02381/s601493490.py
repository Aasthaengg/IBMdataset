import math

while(True):
	n = int(input())
	if n==0:
		break;
	list_str = input().split(' ')
	list_int = []
	sum = 0
	for value in list_str:
		newVar = float(value)
		sum += newVar
		list_int.append(newVar)
	sum /= n
	
	result = 0
	for value in list_int:
		result += (value - sum) * (value - sum)
		
	result = math.sqrt(result / n) if result != 0 else 0
	
	
	print('%.8f'%result)

while True:
	arr = list(map(int, input().split()))
	m = arr[0]
	f = arr[1]
	r = arr[2]
	
	if m == -1 and f == -1 and r == -1:
		break
	
	total = m + f
	if m == -1 or f == -1: print('F')
	elif total >= 80: print('A')
	elif total >= 65: print('B')
	elif total >= 50: print('C')
	elif total >= 30 and r >= 50: print('C')
	elif total >= 30: print('D')
	else: print('F')


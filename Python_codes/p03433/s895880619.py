amount = int(input())
n_1yen = int(input())

fraction = amount % 500

if fraction <= n_1yen:
	print('Yes')
else:
	print('No')    

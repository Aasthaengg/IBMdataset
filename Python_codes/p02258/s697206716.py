n = int( raw_input( ) )

mi = int( raw_input( ) )
profit = 0 - 1000000000
n -= 1
i = 0
while i < n:
	num = int( raw_input( ) )
	
	diff = num - mi
	if profit < diff:
		profit = diff

	if num < mi:
		mi = num
	i += 1

print( profit )
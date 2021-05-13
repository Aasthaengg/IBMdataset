n = int( raw_input( ) )

mi = int( raw_input( ) )
profit = 0 - 1000000000

for i in range( n-1 ):
	num = int( raw_input( ) )
	
	diff = num - mi
	if profit < diff:
		profit = diff

	if num < mi:
		mi = num

print( profit )
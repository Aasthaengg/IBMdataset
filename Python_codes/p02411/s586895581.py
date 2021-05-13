import sys

while True:
	m, f, r = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
	if -1 == m and -1 == f and -1 == r:
		break
	
	mf = ( m + f )
	if -1 == m or -1 == f:
		print( "F" )
	elif 80 <= mf:
		print( "A" )
	elif 65 <= mf and mf < 80:
		print( "B" )
	elif 50 <= mf and mf < 65:
		print( "C" )
	elif 30 <= mf and mf < 50:
		if 50 <= r:
			print( "C" )
		else:
			print( "D" )
	else:
		print( "F" )	
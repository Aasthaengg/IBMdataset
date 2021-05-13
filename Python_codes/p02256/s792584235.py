def gcd( x, y ):
	if 0 == y:
		return x
	else:
		return gcd( y, x%y )
		
a, b = [ int( val ) for val in input( ).split( " " ) ]
if a < b:
	a, b = b, a
print( gcd( a, b ) )
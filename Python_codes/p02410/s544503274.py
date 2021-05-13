import sys

n, m = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
a = [ [ int( val ) for val in sys.stdin.readline().split( " " ) ] for row in range( n ) ]
b = [ [ int( val ) for val in sys.stdin.readline().split( " " ) ] for row in range( m ) ]

for i in range( n ):
	c = 0
	for j in range( m ):
		c += ( a[i][j] * b[j][0] )
	print( c )
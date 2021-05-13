import sys

n, m, l = [ int( val ) for val in sys.stdin.readline().split( " " ) ]

matrixA = [ [ int( val ) for val in sys.stdin.readline().split( " " ) ] for row in range( n ) ]
matrixB = [ [ int( val ) for val in sys.stdin.readline().split( " " ) ] for row in range( m ) ]	
c = 0

output = []
for i in range( n ):
	for j in range( l ):
		c = 0
		for k in range( m ):
			c += ( matrixA[i][k] * matrixB[k][j] )
		output.append( "{:d}".format( c ) )
		output.append( " " )
	output.pop()
	output.append( "\n" )

output.pop()
print( "".join( output ) )
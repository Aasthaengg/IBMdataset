import sys

n = int( sys.stdin.readline() )
output = []
for i in range( 1, n+1 ):
	x = i
	if x%3 == 0:
		output.append( " {:d}".format( i ) )
	else:
		while x:
			if x%10 == 3:
				output.append( " {:d}".format( i ) )
				break
			x /= 10
print( "".join( output ) )
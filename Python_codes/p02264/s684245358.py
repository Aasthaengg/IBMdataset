n, q = [ int( val ) for val in raw_input( ).split( " " ) ]
ps = [0]*n
t = [0]*n
for i in range( n ):
	ps[i], t[i] = raw_input( ).split( " " )


output = []
qsum = 0
while t:
	psi = ps.pop( 0 )
	ti = int( t.pop( 0 ) )
	if ti <= q:
		qsum += ti	
		output.append( psi+" "+str( qsum ) )
	else:
		t.append( ti - q )
		ps.append( psi )
		qsum += q

print( "\n".join( output ) )
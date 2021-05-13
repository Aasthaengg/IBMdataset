s = list( input( ) )
n = int( input( ) )
for i in range( n ):
	cmd = input( ).split( " " )
	a = int( cmd[1] )
	b = int( cmd[2] ) + 1
	if "print" == cmd[0]:
		print( "".join( s[ a:b ] ) )
	elif "reverse" == cmd[0]:
		for i, ss in enumerate( reversed( s[ a:b ] ) ):
			s[ a+i ] = ss
	elif "replace" == cmd[0]:
		for i, ss in enumerate( cmd[3] ):
			s[ a+i ] = ss
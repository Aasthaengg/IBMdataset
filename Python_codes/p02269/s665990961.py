n = int( raw_input( ) )
dic = set()
for i in range( n ):
	cmd, word = raw_input( ).split( " " )
	if "insert" == cmd:
		dic.add( word )
	elif "find" == cmd:
		if word in dic:
			print( "yes" )
		else:
			print( "no" )
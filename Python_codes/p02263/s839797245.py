expressions = raw_input( ).split( " " )
stack = []
for op in expressions:
	if "+" == op:
		b = stack.pop( )
		a = stack.pop( )
		stack.append( a + b )
	elif "-" == op:
		b = stack.pop( )
		a = stack.pop( )
		stack.append( a - b	)
	elif "*" == op:
		b = stack.pop( )
		a = stack.pop( )
		stack.append( a * b )
	else:
		stack.append( int( op ) )
print( stack.pop( ) )
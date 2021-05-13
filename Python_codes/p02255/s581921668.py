n = int( raw_input( ) )
nums = [ int( val ) for val in raw_input( ).split( " " ) ]
print( " ".join( map( str, nums ) ) )

for i in range( 1, len( nums ) ):
	key = nums[i]
	j = i - 1
	while 0 <= j and key < nums[j]:
		nums[ j+1 ] = nums[j]
		j -= 1
	nums[ j+1 ] = key
	print( " ".join( map( str, nums ) ) )
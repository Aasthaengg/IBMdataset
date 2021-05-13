import sys

while True:
	h, w = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
	if 0 ==h and 0 == w:
		break
	print( "{:s}\n".format( "#"*w )*h  )
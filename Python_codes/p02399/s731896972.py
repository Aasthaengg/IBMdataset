import sys

a, b = [ int( val ) for val in sys.stdin.readline().split( ' ' ) ]
print( "{} {}".format( a/b, a%b ) + " %.8f"%( float(a)/float(b) ) )
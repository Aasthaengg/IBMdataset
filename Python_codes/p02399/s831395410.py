import sys

a, b = [ int( val ) for val in sys.stdin.readline().split( ' ' ) ]
print( "{:d} {:d} {:7f}".format( int( a/b ), a%b, a/b ) )
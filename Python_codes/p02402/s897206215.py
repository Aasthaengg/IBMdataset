import sys

n = int( sys.stdin.readline() )
nums = [ int( val ) for val in sys.stdin.readline().split( " " ) ]

print( "{:d} {:d} {:d}".format( min( nums ), max( nums ), sum( nums ) ) )
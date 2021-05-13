import sys

nums = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
nums = sorted( nums )
print( "{:d} {:d} {:d}".format( nums[0], nums[1], nums[2] ) )	
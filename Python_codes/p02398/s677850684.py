import sys

a, b, c = [ int( val ) for val in sys.stdin.readline().split( ' ' ) ]
cnt = 0
for divisor in range( a, b+1 ):
    if ( c % divisor ) == 0:
        cnt += 1
print( "{}".format( cnt ) )
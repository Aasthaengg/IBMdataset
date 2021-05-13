n = int( input() )
#print( n )

#print( range( n-1 ) )

x = 1
y = 1
w = 1
z = 1000000007
for i in range( n ):
    x = ( x % z ) * 10
    y = ( y % z ) * 9
    w = ( w % z ) * 8
#    print( i, x, y )

ans = ( x % z ) - 2 * ( y % z ) + ( w % z )
print( ans % z )

sx,sy,tx,ty = ( int(x) for x in input().split() )

rx = tx - sx
ry = ty - sy

ans = []
# 'U' 'D' 'L' 'R'
# 1
for i in range( ry ):
    ans.append( 'U' )
for i in range( rx ):
    ans.append( 'R' )
# 2
for i in range( ry ):
    ans.append( 'D' )
for i in range( rx ):
    ans.append( 'L' )
# 3
ans.append( 'L' )
for i in range( ry + 1 ):
    ans.append( 'U' )
for i in range( rx + 1 ):
    ans.append( 'R' )
ans.append( 'D' )
# 4
ans.append( 'R' )
for i in range( ry + 1 ):
    ans.append( 'D' )
for i in range( rx + 1 ):
    ans.append( 'L' )
ans.append( 'U' )

print( ''.join(ans) )
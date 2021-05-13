a, b, c, d = map( int, input().split() )
#print( a, b, c, d )

ac = a * c
ad = a * d
bc = b * c
bd = b * d

ans1 = max( ac, bd )
ans2 = max( ad, bc )

ans = max( ans1, ans2 )
print( ans )



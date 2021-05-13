N , R = map( int,input().split() )

if N >= 10:
    print(R)
else:
    Rating = R + ( 1000-  100 * N )
    print(Rating)

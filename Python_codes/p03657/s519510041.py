a,b=(int(x) for x in input().split())
c = ( a + b ) % 3
if ((int(a) % 3)  == 0 or  (int(b) % 3)  == 0 or int(c) == 0):
    print ( 'Possible' )
else:
    print ( 'Impossible' )
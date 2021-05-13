num = int( input() )
group = 0

while( num >= 3 ):
    num -= 3
    group += 1

print( group )
a, b, c, d = map(int, input().split())

AB = abs( b - a )
BC = abs( c - b )
CA = abs( a - c )

if AB <= d and BC <=d:
    print('Yes')
elif CA <= d:
    print('Yes')
else:
    print('No')
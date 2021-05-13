import sys
r,D,x = map(int,input().split())

if not ( 2 <= r <= 5 ): sys.exit()
if not ( 1 <= D <= 100 ): sys.exit()
if not ( D < x <= 200 ): sys.exit()

before_x = x
for I in range(10):
    print( r * before_x - D)
    before_x = r * before_x - D
import math

a,b=list(map(str, input().split()))

if a=='H':
    print(b)
else:
    if b=='H':
        print('D')
    else:
        print('H')
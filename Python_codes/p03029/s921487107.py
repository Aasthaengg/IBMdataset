import math
A, P = map(int, input().split())

if 3*A + P < 2:
    print('0')
else:
    print(math.floor((3*A + P) / 2))

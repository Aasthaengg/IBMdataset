import math
a=math.log10(int(input()))
b=math.log10(int(input()))
if a>b:
    print('GREATER')
elif a==b:
    print('EQUAL')
else:
    print('LESS')

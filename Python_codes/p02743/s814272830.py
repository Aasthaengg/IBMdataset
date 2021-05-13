from math import sqrt
a,b,c=list(map(int,input().split(' ')))
print('Yes' if 4*a*b<(c-a-b)**2 and a+b<c else 'No')
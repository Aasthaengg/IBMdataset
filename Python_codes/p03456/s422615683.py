from math import sqrt,floor,ceil
a,b=input().split(' ')
c=int(a+b)
print('Yes' if floor(sqrt(c)) == ceil(sqrt(c)) else 'No')
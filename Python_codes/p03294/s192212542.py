import math
from functools import reduce

input()
*A,=map(int,input().split())

m=reduce(lambda x,y: (x*y)//math.gcd(x,y), A, 1)
print(sum((m-1)%i for i in A))
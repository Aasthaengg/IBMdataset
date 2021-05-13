from functools import reduce
from operator import add
n=int(input())
print(reduce(add, ((n-1)//a for a in range(1,n))))
import functools
import operator
print('Even' if (functools.reduce(operator.mul,list(map(int,input().split()))))%2==0 else 'Odd')
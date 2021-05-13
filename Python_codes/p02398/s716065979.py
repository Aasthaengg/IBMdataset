from operator import add
from functools import reduce

def divisor_generator(a, b, c):
    for i in range(a, b+1):
        yield (1 if c%i == 0 else 0)

a, b, c = map(int, input().split(' '))

print(reduce(add, divisor_generator(a, b, c)))
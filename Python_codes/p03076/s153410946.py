import sys
import itertools
from decimal import Decimal, ROUND_CEILING
array = [ int(input()) for I in range(5) ]
for I in array:
    if not ( 1 <= I <= 123 ):
        sys.exit()

min = (123 * 5) + (10 * 5)
for J in list(itertools.permutations(array)):
    time = 0
    for K in J[0:-1]:
        time += K
        time = Decimal(time).quantize(Decimal('1E1'), rounding=ROUND_CEILING)
    time += J[-1]
    if min > time: min = time
print(min)
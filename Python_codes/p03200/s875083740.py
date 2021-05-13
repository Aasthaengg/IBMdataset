import numpy
from numpy.core.defchararray import count
S = numpy.array([0 if s == 'B' else 1 for s in input()])

count = 0
bcount = 0

for i, s in enumerate(S):
    if s == 0:
        bcount += 1
    else:
        count += bcount

print(count)
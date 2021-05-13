import numpy

N = int(input())
X0 = N / 1.08
X1 = (N + 1) / 1.08

if numpy.ceil(X1) - numpy.ceil(X0) == 0:
    print(':(')
else:
    print(int(numpy.ceil(X0)))
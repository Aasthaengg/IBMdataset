import numpy
N = int(input())
L = numpy.array(list(map(int, input().split())))

m = numpy.inf

while True:
    if numpy.min(L) == m:
        break

    m = numpy.min(L)
    mi = numpy.argmin(L)

    L = L % m
    L[mi] = m
    L = L[L != 0]

print(numpy.sum(L))
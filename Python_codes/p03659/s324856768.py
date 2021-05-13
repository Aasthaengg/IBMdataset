import numpy
N = int(input())
a = numpy.array(list(map(int, input().split())))

H = numpy.cumsum(a)[:-1]
S = sum(a) - H
print(min(abs(H - S)))
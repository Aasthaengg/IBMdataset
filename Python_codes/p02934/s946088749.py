import numpy
n = int(input())
a = numpy.array(list(map(int,input().split())))
print(1/(1/a).sum())
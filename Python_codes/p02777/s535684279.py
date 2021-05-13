import numpy

S, T = map(str, input().split())
AB = list(map(int, input().split()))
U = input()

if U == S:
    tmp = numpy.array([1,0])
else:
    tmp = numpy.array([0,1])
print(numpy.array(AB-tmp)[0], numpy.array(AB-tmp)[1])
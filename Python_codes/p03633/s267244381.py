
import numpy

n = int(input())
t = [int(input()) for _ in range(n)]

print(numpy.lcm.reduce(t))

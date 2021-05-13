import numpy
N = int(input())
W = []
for i in range(5):
    W.append(int(input()))

M = min(W)
print(int(numpy.ceil(N / M) + 4))
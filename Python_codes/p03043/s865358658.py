import numpy
N, K = map(int, input().split())

p = 0
for i in range(1, N + 1):
    m = numpy.log2(K / i)
    
    if m < 0:
        m = 0
        
    p += 0.5 ** numpy.ceil(m)
    
print(p / N)
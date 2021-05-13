import math
print(' '.join(
    map('{:.6f}'.format,
        map(math.pi.__mul__,
            (lambda x: (x**2, x*2))(float(input()))))))
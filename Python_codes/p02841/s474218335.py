import numpy as np
m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())
x = [30] * 13
x[1] = x[3] = x[5] = x[7] = x[8] = x[10] = x[12] = 31
x[2] = 28
x[0] = 0
print('1' if x[m1] == d1 else '0')

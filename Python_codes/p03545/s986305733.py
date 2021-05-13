from itertools import product
A,B,C,D = list(input())
for k in list(product(['+','-'],repeat=3)):
    k = A + k[0] + B + k[1] + C + k[2] + D
    if eval(k) == 7:
        print('{}=7'.format(k))
        break
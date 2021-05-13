n = int(input())

from fractions import Fraction

for i in range(1,3501):
    for j in range(1,3501):
        if 4*i*j - n*i - n*j > 0:
            if (i * j * n) % (4*i*j - n*i - n*j) == 0 and (i * j * n) // (4*i*j - n*i - n*j) > 0:
                print(i,j, (i * j * n) // (4*i*j - n*i - n*j))
                import sys
                sys.exit()
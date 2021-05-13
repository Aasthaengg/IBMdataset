from fractions import Fraction
import math
N = int(input())
ans = Fraction(4,N)
point = [1,math.floor(N/4)]
for h in range(1,3501):
    h_pro = Fraction(1,h)
    for n in range(1,3501):
        check = ans - h_pro
        n_pro = Fraction(1,n)
        check -= n_pro
        if type(check) == "int":
            if check ==1:
                print(h, end=" ")
                print(n, end=" ")
                print(1)
                exit()
        elif check.numerator == 1:
            print(h, end=" ")
            print(n, end=" ")
            print(check.denominator)
            exit()
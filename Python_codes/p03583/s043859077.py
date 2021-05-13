from fractions import Fraction
import math
N = int(input())
ans = Fraction(4,N)
point = [1,math.floor(N/4)]
for h in range(max(point),3501):
    h_pro = Fraction(1,h)
    check = ans - h_pro
    target = [math.floor(4*h-N/N*h),h]
    for n in range(h,3501):
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
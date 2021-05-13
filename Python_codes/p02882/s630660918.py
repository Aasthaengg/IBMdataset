import math
def resolve():
    a, b, x = list(map(int, input().split()))
    if (a**2)*b/2 > x:
        print(90-math.degrees(math.atan(2*x/((b**2)*a))))
    else:
        if x == (a**2)*b:
            print(0)
        else:
            print(90-math.degrees(math.atan(a**3/(2*(a**2)*b-2*x))))
    

if '__main__' == __name__:
    resolve()

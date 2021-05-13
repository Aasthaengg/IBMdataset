from math import atan,degrees
a,b,x = map(int,input().split())

if x >= a**2*b/2:  # けっっこうおおめ
    print(degrees(atan(2*(a**2*b-x)/a**3) ))
elif x < a**2*b/2:  # すっくねえ
    print(degrees(atan(b**2*a/(2*x))))

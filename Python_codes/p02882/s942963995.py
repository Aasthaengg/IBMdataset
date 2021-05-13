import sys,math
input = sys.stdin.readline
a,b,x = list(map(int,input().split()))
if b*a**2 >= x*2:
    print(90-math.degrees(math.atan(2*x/(a*b**2))))
else:   
    print(math.degrees(math.atan(2*(a**2*b-x)/a**3)))

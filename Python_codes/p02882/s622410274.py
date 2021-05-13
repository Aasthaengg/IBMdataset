import math
a,b,x = map(int,input().split())
v = (a**2)*b
amari = v-x
if amari <= v/2:
    nagasa = amari/a/a*2
    ans = math.atan(nagasa/a)
    ans = ans*360/2/math.pi
    print(ans)
else:
    nagasa = x/b/a*2
    ans = math.pi/2 - math.atan(nagasa/b) 
    ans = ans*360/2/math.pi
    print(ans)
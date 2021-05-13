a,b,x = map(int,input().split())
import math
m_cm3 = a*b*a
if(x >= (m_cm3/2)):
    s = 2*b - (2*x)/(a**2)
    s /= a
    ans = math.degrees(math.atan(s))
else:
    s = (a*b*b)/(2*x)
    ans = math.degrees(math.atan(s))

print(ans)
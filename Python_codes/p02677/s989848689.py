import math
a,b,h,m = map(int,input().split())

thm = m/60 * 2* math.pi 
thh = (h*60 +  m)/720 * 2* math.pi


xm = b * math.cos(thm)
xh = a * math.cos(thh)

ym = b* math.sin(thm)
yh = a* math.sin(thh)

l=math.sqrt((xm-xh)**2 + (ym-yh)**2)
print(l)
import math

(n,m,o) = map(float, raw_input().split())
#s=(n+m+o)/2.0
c=math.radians(o)
cs=math.sqrt(n**2+m**2-2*n*m*math.cos(c))
h=m*math.sin(c)
#ans=(s*(s-m)*(s-n)*(s-o))**0.5
#print ((n-o)**2 + (m-p)**2)**0.5
#print ans
S=h*n/2
L=n+m+cs
print S
print L
print h
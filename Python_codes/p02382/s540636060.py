import math
n=int(input())
p=print
i=input
a=[int(s) for s in i().split()]
b=[int(s) for s in i().split()]
m1=0
m2=0
m3=0
m4=0
for x,y in zip(a,b):
    fabs=math.fabs(x-y)
    m1+=fabs
    m2+=fabs**2
    m3+=fabs**3
    m4=max(fabs,m4)
p(m1)
p(pow(m2,1/2))
p(pow(m3,1/3))
p(m4)

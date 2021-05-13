import math

n=int(input())
t,a=map(int,input().split())
vt=t
va=a
for i in range(1,n):
    t, a = map(int, input().split())
    if vt<=t and va<=a:
        vt=t
        va=a
    elif vt>t and va<=a:
        x=-(-vt//t)
        vt,va=x*t,x*a
    elif vt<=t and va>a:
        x=-(-va//a)
        vt,va=x*t,x*a
    else:
        x1 = -(-vt // t)
        x2 = -(-va // a)
        if x1*t+x1*a >=x2*t+x2*a:
            vt, va = x1 * t, x1 * a
        else:
            vt, va = x2 * t, x2 * a

print(va+vt)
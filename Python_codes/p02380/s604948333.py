import math
a=[float(i)for i in input().split()]
k=a[2]*math.pi/180
if a[2]>90.0:
    h=math.sin(k)*a[1]
    s=math.cos(k)*a[1]
    L=math.sqrt((a[0]-s)*(a[0]-s)+h*h)+a[0]+a[1]
elif a[2]<90.0:
    h=math.sin(k)*a[1]
    n=math.sqrt(a[1]*a[1]-h*h)
    L=a[0]+a[1]+math.sqrt(h*h+(a[0]-n)*(a[0]-n))
else:
    h=a[1]
    L=math.sqrt(a[0]*a[0]+a[1]*a[1])+a[0]+a[1]
S=a[0]*h/2
print("%.5f"%(S))
print("%.5f"%(L))
print("%.5f"%(h))
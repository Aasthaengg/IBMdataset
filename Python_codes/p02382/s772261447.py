import math
n=int(input())
x=[float(i) for i in input().split()]
y=[float(i) for i in input().split()]
z=[float(0)for i in range(len(x))]
count=0.0
for i in range(len(x)):
    z[i]=abs(x[i]-y[i])
    count=count+abs(x[i]-y[i])
print("%.5f"%count)
count=0.0
for i in range(len(x)):
    count=count+abs(x[i]-y[i])*abs(x[i]-y[i])
print("%.5f"%math.sqrt(count))
count=0.0
for i in range(len(x)):
    count=count+abs(x[i]-y[i])*abs(x[i]-y[i])*abs(x[i]-y[i])
print("%.5f"%math.pow(count,(1.0/3.0)))
print("%.5f"%max(z))
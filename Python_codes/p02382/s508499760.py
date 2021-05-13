import math
n=int(raw_input())
x=list(map(int,raw_input().split()))
y=list(map(int,raw_input().split()))
z=[0]*n
zz=[0]*n
zzz=[0]*n
for i in range(n):
	x.append(y[i])
for i in range(n):
	z[i]=math.fabs(x[i]-x[n+i])
	zz[i]=z[i]**2
	zzz[i]=z[i]**3
print sum(z)
print math.sqrt(sum(zz))
print sum(zzz)**(1/3.0)
print max(z)
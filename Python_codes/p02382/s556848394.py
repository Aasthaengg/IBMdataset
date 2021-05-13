import math
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z,a,b=[],0,0
for i in range(n):
    z.append(abs(x[i]-y[i]))
for i in range(n):
    a+=(z[i]**2)
    b+=(z[i]**3)
a=math.sqrt(a)
b=math.pow(b,1.0/3.0)
print('{:.6f}\n{:.6f}\n{:.6f}\n{:.6f}'.format(sum(z),a,b,max(z)))

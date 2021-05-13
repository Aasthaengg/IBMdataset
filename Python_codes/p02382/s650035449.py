n=int(input())
x=list(map(int,input().split()))

y=list(map(int,input().split()))
z=[0]*n
a=0
b=0
c=0
d=0
for i in range(n):
    a=a+abs(x[i]-y[i])
    b=b+(x[i]-y[i])**2
    c=c+abs(x[i]-y[i])**3
    z[i]=abs(x[i]-y[i])
print(f'{a:.10f}')
b=b**(1/2)
print(f'{b:.10f}')
c=c**(1/3)
print(f'{c:.10f}')
print(f'{max(z):.10f}')

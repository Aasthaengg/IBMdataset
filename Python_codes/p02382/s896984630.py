import math
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
d1=0
d2=0
d3=0
D1=[]
for i in range(n):
    d1+=abs(x[i]-y[i])
print(f'{d1:.6f}')
for i in range(n) :
    d2+=abs(x[i]-y[i])**2
print(f'{math.pow(d2,1/2):.6f}')
for i in range(n):
    d3+=abs(x[i]-y[i])**3
print(f'{math.pow(d3,1/3):.6f}')
for i in range(n):
    D1.append(abs(x[i]-y[i]))
print(f'{max(D1):.6f}')

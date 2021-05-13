import itertools
x=[0]*1000
r,D,x[0]=map(int,input().split())

for i in range(0,99):
    x[i+1]=r*x[i]-D
for i in range(10):
    print(x[i+1])

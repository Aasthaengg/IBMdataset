import math

N=int(input())
a=100000

for i in range(N):
    b=a/1000
    a=math.ceil(b*1.05)
    a=a*1000
    
print(a)

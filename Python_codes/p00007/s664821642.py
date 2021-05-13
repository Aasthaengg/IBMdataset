import math
N=int(input())
a=100000
for i in range(N):
    a=a*1.05
    a=math.ceil(a/1000)*1000
print(a)

import math

s=int(input())
t=100

for i in range(0,s):
    t=math.ceil(t*1.05)
print(1000*t)

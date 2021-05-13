import math
a=int(input())
A=100
for i in range(a):
    A=math.ceil(A*1.05)
print(A*1000)

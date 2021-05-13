import math
n=input()
n=int(n)
a=100000
for i in range(n):
    a=a*1.05
    a=math.ceil(a/1000)*1000
print(a)    
